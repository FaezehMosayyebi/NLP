"""
    Stemming
    in stemming we want to finde the stem of words.
"""

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Defining stemmer
ps = PorterStemmer()

text = "Hi my name is Faezeh and I am riding a car."

# Tokenizing words
words = word_tokenize(text)

# Finding the stems of the words
for w in words:
    print(ps.stem(w))