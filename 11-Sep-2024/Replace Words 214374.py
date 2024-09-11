# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(lambda : None)

 

class Solution:
    def __init__(self):
        self.root =  TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if cur.children[c] == None:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.addWord(word)

        ans = ""
        for word in sentence.split():
            if word[0] not in self.root.children:
                ans += word + " "
            else:
                cur = self.root
                tempVar = ""
                for c in word:
                    if cur.is_end:
                        ans += tempVar + " "
                        break
                    if cur.children[c] == None:
                        ans += word + " "
                        break
                    tempVar += c
                    cur = cur.children[c]
                else:
                    ans += word + " "
        return ans[:-1]

