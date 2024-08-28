# Problem: String Without AAA or BBB - https://leetcode.com/problems/string-without-aaa-or-bbb

class Solution(object):
    def strWithout3a3b(self, A, B):
        ans = []

        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B

            if writeA:
                A -= 1
                ans.append('a')
            else:
                B -= 1
                ans.append('b')

        return "".join(ans)