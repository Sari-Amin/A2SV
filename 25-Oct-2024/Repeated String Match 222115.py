# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
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
                    return True

            return False


        if len(a) >= len(b):
            one = kmp(a,b)
            two = kmp(a+a, b)
            if one:
                return 1
            elif two:
                return 2
            else:
                return -1
        else:
            diff = len(b) - len(a)
            ans = ceil(diff / len(a))
            a += (a * ans)
            one = kmp(a,b)
            two = kmp(a+a, b)
            if one:
                return ans + 1
            elif two:
                return ans + 2
            else:
                return -1

    