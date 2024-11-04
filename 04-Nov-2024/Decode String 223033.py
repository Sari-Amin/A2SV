# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in s:
            if i != "]":
                st.append(i)
            else:
                temp = []
                while len(st) > 0 and st[-1].isalpha():
                    temp.append(st.pop())
                st.pop()
                num = ""
                while len(st) > 0 and st[-1] in "0123456789":
                    num += st.pop()
           
                st.append("".join(temp[::-1]) * int(num[::-1]))
           
        return "".join(st)
