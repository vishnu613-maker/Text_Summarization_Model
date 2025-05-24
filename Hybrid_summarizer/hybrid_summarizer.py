import nltk
from .utils import smart_capitalize_sentences

def chunk_text(text, max_words=400, overlap=50):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i+max_words]
        chunks.append(" ".join(chunk))
        i += max_words - overlap
    return chunks

def hybrid_summarize(
    article,
    extractor,
    abstracter,
    tokenizer,
    num_sentences=5,
    max_abstractive_tokens=128,
    desired_word_count=60,
    chunk_words=400,
    chunk_overlap=50
):
    article_chunks = chunk_text(article, max_words=chunk_words, overlap=chunk_overlap)
    chunk_summaries = []
    for chunk in article_chunks:
        sentence_count = chunk.count('.') + chunk.count('!') + chunk.count('?')
        word_count = len(chunk.split())
        if sentence_count < 2 or word_count < 30:
            extracted = chunk
        else:
            try:
                extracted = extractor(chunk, num_sentences=min(num_sentences, sentence_count))
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
