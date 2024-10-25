# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def kmp(s,p):
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
            n = len(s) 
            m = len(p)
            l = 0
            r = 0
            while r < n:
                if p[l] == s[r]:
                    l += 1
                    r += 1
                else:
                    if l == 0:
                        r += 1
                    else:
                        l = lps[l - 1]

                if l == m:
                    return r - m

            return -1

        return kmp(haystack, needle)





