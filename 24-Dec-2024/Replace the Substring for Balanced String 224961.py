# Problem: Replace the Substring for Balanced String - https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution:
    def balancedString(self, s: str) -> int:
        freq = Counter(s)
        tobe = len(s) // 4
        extras = {}
        for key in freq:
            if freq[key] > tobe:
                extras[key] = freq[key] - tobe
        
        if not extras: return 0
        i = 0
        ans = len(s)
        for j in range(len(s)):
            if s[j] in extras:
                extras[s[j]] -= 1
            
            while max(extras.values()) <= 0:
                ans = min(ans, j-i+1)
                if s[i] in extras:
                    extras[s[i]] += 1
                i += 1
                
                
        return ans