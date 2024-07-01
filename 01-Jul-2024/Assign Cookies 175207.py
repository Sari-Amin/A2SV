# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        left = 0
        right = 0
        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                ans += 1
                left += 1

            right += 1
        
        return ans