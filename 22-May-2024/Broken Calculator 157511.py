# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # if startValue >= target:
        #     return startValue - target
    
        # if target % 2 == 0:
        #     return 1 + self.brokenCalc(startValue, target // 2)

        # return 1 + self.brokenCalc(startValue, target + 1)
        ans = 0
        while target > startValue:
            if target % 2:
                ans += 1
                target += 1
            else:
                ans += 1
                target //= 2
        if startValue >= target:
            ans += startValue - target
        return ans