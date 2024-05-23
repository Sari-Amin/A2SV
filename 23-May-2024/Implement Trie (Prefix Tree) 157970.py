# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(lambda : None)

class Trie:

    def __init__(self):
        self.root =  TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if cur.children[c] == None:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if cur.children[c] == None:
                return False
            cur = cur.children[c]
        return cur.is_end 

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if cur.children[c] == None:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)