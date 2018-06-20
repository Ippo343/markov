#!/usr/bin/env python3
# -*- coding: utf8 -*-

from collections import defaultdict
from numpy import random


class FreqTable:

    def __init__(self):
        self._total = 0
        self._data = defaultdict(int)
        self._precomputed_freq = None

    def add(self, token):
        self._data[token] += 1
        self._total += 1
        self._precomputed_freq = None

    def __getitem__(self, item):
        return self._data.get(item, 0) / self._total

    def _precompute_freq(self):

        tokens = list(self._data.keys())
        weights = [self[t] for t in tokens]
        self._precomputed_freq = (tokens, weights)

    def choose(self):
        try:

            if not self._precomputed_freq:
                self._precompute_freq()

            tokens, weights = self._precomputed_freq
            choice = random.choice(tokens, p=weights)

            return choice

        except Exception as e:
            return None


class Chain:

    def __init__(self, order=2):
        self._tables = defaultdict(FreqTable)
        self._order = order
        self._reset_state()

    def _reset_state(self):
        self._state = [None] * self._order

    def _push_state(self, token):
        self._state.pop(0)
        self._state.append(token)

    def feed(self, tokens):
        self._reset_state()
        for token in tokens:
            self._tables[tuple(self._state)].add(token)
            self._push_state(token)

    def generate(self):
        self._reset_state()

        def generator_helper():
            while True:
                token = self._tables[tuple(self._state)].choose()

                if token is None:
                    return

                self._push_state(token)
                yield token

        return " ".join(generator_helper())
