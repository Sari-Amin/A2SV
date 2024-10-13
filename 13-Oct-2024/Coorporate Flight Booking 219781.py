# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0] * n
        for l, r, val in bookings:
            if r != n:
                prefix_sum[r] -= val
            prefix_sum[l - 1] += val
        for i in range(1,n):
            prefix_sum[i] += prefix_sum[i - 1]
        return prefix_sum