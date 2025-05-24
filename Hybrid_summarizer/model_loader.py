from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_abstracter(model_dir):
    """
    Loads the abstractive summarization model (e.g., T5/BART) and its tokenizer.
    """
    abstracter = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    return abstracter, tokenizer
