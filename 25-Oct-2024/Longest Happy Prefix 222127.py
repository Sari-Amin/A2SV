# Problem: Longest Happy Prefix - https://leetcode.com/problems/longest-happy-prefix/description/

class Solution:
    def longestPrefix(self, s: str) -> str:
        def kmp(p):
            n = len(p) 
            lps = [0 for _ in range(n)]
            l = 0
            r = 1
            while r < n:
                if p[l] == p[r]:
                    lps[r] = l + 1
                    l += 1
                    r += 1
                else:
                    if l == 0:
                        r += 1
                    else:
                        l = lps[l - 1]
            return lps

        lps = kmp(s)
        
        return s[:lps[-1]]