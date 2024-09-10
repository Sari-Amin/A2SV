# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack=0, '+', []
        for char in s+'+':
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-*/":
                if sign=='+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(math.trunc(stack.pop()/num))
                sign = char
                num = 0             
        return sum(stack)