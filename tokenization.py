"""
    Tokenize
    We want to divide the text into sentences and words.
"""
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Hello! My name is Faezeh. I am an AI expert."

print(sent_tokenize(text))
print(word_tokenize(text))