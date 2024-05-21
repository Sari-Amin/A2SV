# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtrack(ind, st = []):
            if len(st) == len(s):
                ans.append("".join(st[:]))
                return 
            if ind >= len(s):
                return
            

            for i in range(ind, len(s)):
                if s[i].isalpha():
                    #upper case
                    st.append(s[i].upper())
                    backtrack(i + 1, st)
                    st.pop()
                    #lower case
                    st.append(s[i].lower())
                    backtrack(i + 1, st)
                    st.pop()
                else:
                    st.append(s[i])
                    backtrack(i + 1, st)
                    st.pop()
        backtrack(0)
        return ans
