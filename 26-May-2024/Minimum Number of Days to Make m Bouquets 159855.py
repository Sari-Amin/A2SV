# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(mid):
            fl, b = 0, 0
            for d in bloomDay:
                fl = fl + 1 if d <= mid else 0
                if fl == k:
                    b += 1
                    if b == m:
                        break
                    fl = 0
            return b == m

        if len(bloomDay) < m * k:
            return -1

        left = 1
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2

            day =  possible(mid)
            if day:
                right = mid 
            else:
                left = mid + 1
        return left