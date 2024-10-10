# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {}
        for i in "qwertyuiop":
            dic[i] = 1
        for i in "asdfghjkl":
            dic[i] = 2
        for i in "zxcvbnm":
            dic[i] = 3
             
        ans = []
        for word in words:
            temp = set()
            for ch in word.lower():
                temp.add(dic.get(ch, 0))
            if len(temp) == 1:
                ans.append(word)
        return ans