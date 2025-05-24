import nltk
from .utils import smart_capitalize_sentences
from sentence_transformers import SentenceTransformer, util

# Ensure NLTK punkt is available (safe to call repeatedly)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def chunk_text(text, max_words=400, overlap=50):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i+max_words]
        chunks.append(" ".join(chunk))
        i += max_words - overlap
    return chunks

def extractive_summary(text, num_sentences=5):
    """
    Extract the most representative sentences from the text using sentence-transformers.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')
    # Use nltk to split into sentences
    sentences = [s.strip() for s in nltk.sent_tokenize(text) if len(s.strip()) > 20]
    if not sentences:
        return text
    # Get embeddings
    embeddings = model.encode(sentences)
    doc_embedding = model.encode([text])
    scores = util.cos_sim(embeddings, doc_embedding)[..., 0]
    # Get indices of top N sentences
    top_indices = scores.argsort(descending=True)[:num_sentences]
    # Return sentences in original order
    summary = ' '.join([sentences[i] for i in sorted(top_indices.cpu().numpy())])
    return summary

def hybrid_summarize(
    article,
    abstracter,
    tokenizer,
    num_sentences=5,
    max_abstractive_tokens=128,
    desired_word_count=60,
    chunk_words=400,
    chunk_overlap=50
):
    """
    Hybrid extractive-abstractive summarization.
    1. Chunk the article if it's long.
    2. For each chunk, extract key sentences.
    3. Pass the extractive summary to the abstractive model.
    4. Concatenate and trim the final summary.
    """
    article_chunks = chunk_text(article, max_words=chunk_words, overlap=chunk_overlap)
    chunk_summaries = []
    for chunk in article_chunks:
        sentence_count = chunk.count('.') + chunk.count('!') + chunk.count('?')
        word_count = len(chunk.split())
        if sentence_count < 2 or word_count < 30:
            extracted = chunk
        else:
            try:
                extracted = extractive_summary(chunk, num_sentences=min(num_sentences, sentence_count))
            except Exception:
                extracted = chunk
        input_text = "summarize: " + extracted
        inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = abstracter.generate(
            inputs,
            max_length=max_abstractive_tokens,
            min_length=int(max_abstractive_tokens * 0.6),
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        chunk_summaries.append(summary)
    combined_summary = " ".join(chunk_summaries)
    words = combined_summary.split()
    final_summary = " ".join(words[:desired_word_count])
    final_summary = smart_capitalize_sentences(final_summary)
    return final_summary
