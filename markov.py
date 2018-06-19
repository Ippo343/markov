import itertools
from collections import defaultdict
from numpy import random


class FreqTable:

    def __init__(self):
        self._total = 0
        self._data = defaultdict(int)

    def add(self, token):
        self._data[token] += 1
        self._total += 1

    def __getitem__(self, item):
        return self._data.get(item, 0) / self._total

    def choose(self):
        try:
            tokens = list(self._data.keys())
            weights = [self[t] for t in tokens]

            choice = random.choice(tokens, p=weights)
            return choice
        except:
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

        while True:
            token = self._tables[tuple(self._state)].choose()

            if token is None:
                return

            self._push_state(token)
            yield token
