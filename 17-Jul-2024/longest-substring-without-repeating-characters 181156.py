# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = 1
        l,r = 0, 0
        counter = defaultdict(int)
        while r < len(s):
          
            counter[s[r]] += 1
            while l < r and counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            r += 1
       
            ans = max(ans, r - l)
        return ans