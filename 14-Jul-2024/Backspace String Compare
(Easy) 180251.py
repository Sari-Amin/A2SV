# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(s):
            st = []
            for ch in s:
                if ch == "#":
                    if st:
                        st.pop()
                else:
                    st.append(ch)
            return st
        
        return helper(s) == helper(t)
        