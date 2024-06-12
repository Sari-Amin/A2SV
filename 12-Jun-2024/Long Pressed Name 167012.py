# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        l = 0
        r = 0
        while r < len(typed) and l < len(name):
            if name[l] == typed[r]:
                temp = name[l]
                counter = 0
                while l < len(name) and temp == name[l]:
                    l += 1
                    counter += 1
                temp = typed[r]
                counter1 = 0
                while r < len(typed) and temp == typed[r]:
                    r += 1
                    counter1 += 1
                if counter > counter1:
                    return False
            else:
                return False
        if l < len(name) or r < len(typed):
            return False
        return True