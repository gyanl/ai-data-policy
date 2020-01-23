## Find freq dist of book

import nltk
from nltk import *

f = open('darkness.txt', 'r')
raw = f.read().decode('utf8')

tokens = word_tokenize(raw)
mybook = nltk.Text(tokens)

## Print words used in context similar to 'people'.
mybook.similar('people')

## Create FreqDist object fd
fd = FreqDist(mybook)

## Print freq. of 50 most common words.
print(fd.most_common(50))

## Use matplotlib to plot freq of 50 most common words
fd.plot(50)
