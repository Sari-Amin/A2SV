# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # if startValue >= target:
        #     return startValue - target
    
        # if target % 2 == 0:
        #     return 1 + self.brokenCalc(startValue, target // 2)

        # return 1 + self.brokenCalc(startValue, target + 1)
        res = 0
        while target > startValue:
            if target % 2:
                res += 1
                target += 1
            else:
                res += 1
                target //= 2
        if startValue >= target:
            res += startValue - target
        return res