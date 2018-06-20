#!/usr/bin/env python3
# -*- coding: utf8 -*-

import itertools
from nltk import sent_tokenize, word_tokenize
import markov

if __name__ == '__main__':

    with open('text') as f:
        data = f.read()

    sentences = sent_tokenize(data)
    chain = markov.Chain(order=3)

    for i, s in enumerate(sentences):
        if not i % 1000:
            print(i)
        chain.feed(word_tokenize(s))

    for i in range(10):
        print(chain.generate())
