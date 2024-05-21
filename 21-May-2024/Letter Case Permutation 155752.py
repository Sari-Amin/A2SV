# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        used = 0
        def backtrack(ind, st = []):
            nonlocal used
            if len(st) == len(s):
                ans.append("".join(st[:]))
                return 
            if ind >= len(s):
                return
            

            for i in range(ind, len(s)):
                if used & 1 << i == 0:
                    if s[i].isalpha():
                        #upper case
                        st.append(s[i].upper())
                        used |= 1 << i
                        backtrack(i + 1, st)
                        st.pop()
                        used &= ~(1 << i)
                        #lower case
                        st.append(s[i].lower())
                        used |= 1 << i

                        backtrack(i + 1, st)
                        st.pop()
                        used &= ~(1 << i)


                    else:
                        st.append(s[i])
                        used |= 1 << i
                        backtrack(i + 1, st)
                        st.pop()
                        used &= ~(1 << i)


        backtrack(0)
        return ans
