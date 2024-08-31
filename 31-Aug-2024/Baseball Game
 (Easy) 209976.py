# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for  c in operations:
            if c == "C":
                if stack:
                    stack.pop()
            elif c == "D":
                stack.append(int(stack[-1]) * 2)
            elif c == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            else:
                stack.append(c)
        return sum([int(i) for i in stack])