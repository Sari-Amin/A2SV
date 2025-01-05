# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ")":
                temp = ""
                while stack and stack[-1] != "(":
                    temp += stack.pop()
                if stack:
                    stack.pop()
                stack.extend(temp)
            else:
                stack.append(ch) 
                
        return "".join(stack)
