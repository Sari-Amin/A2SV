# Problem: Corporate Flight Bookings - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for l, r, val in bookings:
            if r != n:
                ans[r] -= val
            ans[l - 1] += val
        for i in range(1,n):
            ans[i] += ans[i - 1]
        return ans