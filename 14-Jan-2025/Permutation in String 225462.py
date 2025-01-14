# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        count = [0] * 26

        ln = len(s1)
        cnt = ln
        for ch in s1:
            count[ord(ch) - ord('a')] += 1

        while right < len(s2):
            if right - left + 1 <= ln:
                if count[ord(s2[right]) - ord('a')] > 0:
                    cnt -= 1
                count[ord(s2[right]) - ord('a')] -= 1
                right += 1
                if cnt == 0:
                    return True
            else:
                count[ord(s2[left]) - ord('a')] += 1
                if count[ord(s2[left]) - ord('a')] > 0:
                    cnt += 1
                left += 1
        return False
