# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(lambda : None)

class WordDictionary:

    def __init__(self):
        self.root =  TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if cur.children[c] == None:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        left = 0
        queue = deque([(self.root, "")])

        while left < len(word):

            for i in range(len(queue)):
                node = queue.popleft()
                if word[left] == ".":
                    for ch in node[0].children:
                        queue.append((node[0].children[ch], node[1] + "."))
                elif word[left] in node[0].children:
                    queue.append((node[0].children[word[left]], node[1] + word[left]))

            left += 1

        for i in range(len(queue)):
            node = queue.popleft()
            if node[0].is_end:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)