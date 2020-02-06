## Find freq dist of book

import nltk
from nltk import *

f = open('constitution.txt', 'r')
raw = f.read().decode('utf8')

tokens = word_tokenize(raw)
mybook = nltk.Text(tokens)

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word + " ")
        word = cfdist[word].max()

## Print bigrams of book.
bigrams = nltk.bigrams(mybook)
cfd = nltk.ConditionalFreqDist(bigrams)

## print(cfd['Tharoor'])
## print(generate_model(cfd, 'Tharoor'))

mybook.similar("people")
