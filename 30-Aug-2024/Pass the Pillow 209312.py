# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        dirc = True
        ans = 1
        while time:
            if dirc:
                ans += 1
                if ans == n:
                    dirc = not dirc
            else:
                ans -= 1
                if ans == 1:
                    dirc = not dirc
            time -= 1
        return ans
