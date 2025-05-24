import re

def smart_capitalize_sentences(text):
    sentences = re.split('([.!?] *)', text)
    new_sentences = []
    for i in range(0, len(sentences)-1, 2):
        sentence = sentences[i].strip()
        if sentence:
            sentence = sentence[0].upper() + sentence[1:]
        new_sentences.append(sentence + sentences[i+1].strip())
    if len(sentences) % 2 != 0:
        new_sentences.append(sentences[-1])
    return ' '.join(new_sentences)
