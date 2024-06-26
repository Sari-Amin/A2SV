# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def possible(lim, cnt):
            res = 1
            ptr = 0
            ri  = 0

            while ptr < len(position) and ri < len(position):
  
                if position[ri] - position[ptr] >= lim:
                    res += 1
                    if res == cnt:
                        return True
                    ptr = ri
                else:
                    ri += 1

            return cnt <= res


        left = 1
        right = position[-1] - position[0]
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
      
            if possible(mid,m):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans