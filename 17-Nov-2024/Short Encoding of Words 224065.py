# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ends = []

    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        self.ends.append((root, len(word) + 1))

class Solution:
    def minimumLengthEncoding(self, words):
        trie, ans = Trie(), 0
        
        for word in set(words):
            trie.insert(word[::-1])
        for nd, dp in trie.ends:
            if len(nd.children) == 0:
                ans += dp

        return ans