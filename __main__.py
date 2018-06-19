#!/usr/bin/env python3
# -*- coding: utf8 -*-

import itertools
from nltk import sent_tokenize, word_tokenize
import markov

if __name__ == '__main__':

    with open('text') as f:
        data = list(filter(None, map(str.strip, f.readlines())))

    sentences = list(itertools.chain(*(sent_tokenize(s) for s in data)))

    chain = markov.Chain()
    for s in sentences:
        chain.feed(word_tokenize(s))

    for t in chain.generate():
        print(t, end=' ')

    print("")
