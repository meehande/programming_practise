import numpy as np
from typing import List

LETTERS = 'abcdefghijklmnopqrstuvwxyz'


class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = np.array([None]*len(LETTERS))


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        curr_node = self.root
        for w in word:

            if w not in LETTERS:
                raise ValueError(f'expected letter, got: {w}')

            char_index = LETTERS.index(w)
            if (next_node := curr_node.children[char_index]) is None:
                curr_node.children[char_index] = Node()
                next_node = curr_node.children[char_index]
            curr_node = next_node
        curr_node.value = True

    def search(self, word: str):
        curr_node = self.root
        for w in word:

            if w not in LETTERS:
                raise ValueError(f'expected letter, got: {w}')

            char_index = LETTERS.index(w)
            if curr_node.children[char_index] is None:
                return False
            curr_node = curr_node.children[char_index]
        return curr_node.value is not None

    def remove(self, word):
        curr_node = self.root
        for w in word:

            if w not in LETTERS:
                raise ValueError(f'expected letter, got: {w}')

            char_index = LETTERS.index(w)
            if curr_node.children[char_index] is None:
                return False
            curr_node = curr_node.children[char_index]
        curr_node.value = None
        if all([cc is None for cc in curr_node.children]):
            curr_node = None
        return True

    def print(self):
        pass


def build_trie(words: List[str]):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie


trie = build_trie(['word', 'well', 'we'])

trie.search('we')
trie.remove('we')
trie.search('we')
