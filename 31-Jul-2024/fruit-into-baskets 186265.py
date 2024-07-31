# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        l = 0
        r = 0
        ans = 0
        while r < len(fruits):
            if fruits[r] not in freq:
                freq[fruits[r]] = 1
            else:
                freq[fruits[r]] += 1
            while len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans