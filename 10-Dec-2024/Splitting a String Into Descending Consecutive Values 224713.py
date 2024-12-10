# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(ind, path = []):
            if ind == len(s):
                if len(path) >= 2:
                    return True
                return False
            
            for i in range(ind, len(s)):
                temp = int(s[ind:i + 1])
                if not path or path[-1] - temp == 1:
                    path.append(temp)
                    if backtrack(i + 1, path):
                        return True
                    path.pop()

            return False

        return backtrack(0)