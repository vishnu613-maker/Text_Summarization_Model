from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModel
from summarizer import Summarizer  # external library

def load_abstracter(model_dir):
    abstracter = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    return abstracter, tokenizer

def load_extractor(model_dir):
    bert_model = AutoModel.from_pretrained(model_dir)
    bert_tokenizer = AutoTokenizer.from_pretrained(model_dir)
    extractor = Summarizer(model_dir)  # Pass path as string
    return extractor