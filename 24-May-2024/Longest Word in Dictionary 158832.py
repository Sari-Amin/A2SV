# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

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

    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.addWord(word)
        
        queue = deque([(self.root, "")])
        ans = ""
        while queue:
            node, st = queue.popleft()
            for nd in node.children:
                if node.children[nd].is_end:
                    if len(ans) < len(st + nd):
                        ans = st + nd
                    if ans > st + nd:
                        ans = st + nd
                    queue.append((node.children[nd],st + nd))
        return ans