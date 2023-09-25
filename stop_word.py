"""
    Deleting Stop Words
    Some words are not important for us and even without them, we can understand the meaning of the sentence.
    So we remove them to reduce the amount of data to process.
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = """CODE is founded by Mr. Bachem. Studying at CODE will be unlike 
any other higher education experience. Our intensive, interdisciplinary 
bachelor’s programs are designed to dramatically improve the way you work 
and to prepare you for the reality of tomorrow’s workplace."""

# Defining the stop word in a specific language
stop_words = set(stopwords.words('english'))

# Tokenizing words to divide the text into words.
tokens = word_tokenize(text)

# Filtering the sentence and deleting stop words.
# Solution 1
filtred_sentence = [w for w in tokens if not w in stop_words]

# Solution 2
filtred_sentence = []
for w in tokens:
    if w not in stop_words:
        filtred_sentence.append(w)

print(filtred_sentence)