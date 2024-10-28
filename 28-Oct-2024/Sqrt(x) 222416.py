# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
       
        left = 0
        right = x

        while left + 1 < right:

            md = left + (right - left) // 2
   
            if md * md == x:
                return md
            elif md * md < x:
                left = md 
            else:
                right = md 


        if  right * right == x: return right
        return left
