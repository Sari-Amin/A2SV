# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = [0] * 26

        for ch in p:
            count[ord(ch) - ord("a")] += 1
        
        cnt = len(p)
        pLen = len(p)
        left = 0
        right = 0
        ans = []
        while right < len(s):

            if (right - left + 1) <= pLen:
                if count[ord(s[right]) - ord("a")] > 0:
                    cnt -= 1
                count[ord(s[right]) - ord("a")] -= 1
                right += 1
                if cnt == 0:
                    ans.append(left)
            else:
                count[ord(s[left]) - ord("a")] += 1
                if count[ord(s[left]) - ord("a")] > 0:
                    cnt += 1
                left += 1

        return ans