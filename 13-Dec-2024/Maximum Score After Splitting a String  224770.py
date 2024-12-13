# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        number_of_ones = s.count("1") - int(s[0])
        lsum = s[0] == "0"
        max_score = 0
        for ch in s[1:-1]:

            max_score = max(max_score, lsum + number_of_ones)
            
            if ch == "1":
                number_of_ones -= 1
            else:
                lsum += 1

        max_score = max(max_score, lsum + number_of_ones)
        
        return max_score