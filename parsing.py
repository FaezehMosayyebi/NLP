"""
    Speech tagging
    speeh tagging in nltk reffers to labeling word of a text as their role in a sentence. e.g. noune, verb, ...
"""

import nltk 
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import gutenberg

class speech_tagger:
    def __init__(self, gutenberg_field:str):

        # Downloadin a small part of text in gutenberg project
        #nltk.download('gutenberg')

        # The following is used to tagging words with their parts of speech
        #nltk.download('averaged_perceptron_tagger')

        # Setting raw data of different fields of gutenberg as test and train data
        train = gutenberg.raw(gutenberg_field)

        """
            PunktSentenceTokenizer uses an unsupervised algorithm to build a model for abbreviation words,
            collocations, and words that start sentences; and then uses that model to find sentence boundaries.
        """

        # Train tokenizer on the predefined train data
        self.custom_sent_tokenizer = PunktSentenceTokenizer(train)

    def tag(self, text):

        # Use the trained tokenizer model to tokenize test data
        tokenized = self.custom_sent_tokenizer.tokenize(text)

        tagged_txt = []

        try:
            for i in tokenized:
                actual_words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(actual_words)
                tagged_txt = tagged_txt + tagged
            print(f'Tagged text: {tagged_txt}')
            return (tagged_txt)

        except Exception as e:
            print(str(e))

class chunker:
    def __init__(self, grammer:str):
        grammer = "NP: {<DT>?<JJ>*<NN>}"
        self.cp = nltk.RegexpParser(grammar=grammer)

    def chunking(self, tagged_txt):
        result = self.cp.parse(tagged_txt) 
        print(f'Text chunkes: {result}')
        return result

            

if __name__ == '__main__':
    tagger = speech_tagger("chesterton-brown.txt")
    chunk = chunker("NP: {<DT>?<JJ>*<NN>}")
    text = "The huge dog barked at the cat."
    tegged_txt = tagger.tag(text)
    chunked_txt = chunk.chunking(tegged_txt)
