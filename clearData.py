import re
import pickle as pk

def clear_text(file, stopword_file):
    res = pk.load(open(file, 'rb'))
    words = []
    for text in res:
        words.extend(re.split('\W+', text))

    stopwords = open(stopword_file, 'r')
    stopwords = [i.strip() for i in list(stopwords)]
    words = [word.lower() for word in words if word != '']
    text = ' '.join(words)

    return text, stopwords