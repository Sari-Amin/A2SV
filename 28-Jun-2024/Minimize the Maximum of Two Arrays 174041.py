# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        left = 1
        right = 10**15
        ans = right 
        lcm = (divisor1 * divisor2) // gcd(divisor1, divisor2)
        while left <= right:
            mid = left + (right - left) // 2

            if divisor1 == divisor2:
                free = mid - mid // divisor1
                if free >= uniqueCnt1 + uniqueCnt2:
                    ans =  mid
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                tempCnt1 = uniqueCnt1
                tempCnt2 = uniqueCnt2
                common = mid // lcm
                divisorOf1 = mid // divisor1 - common
                divisorOf2 = mid // divisor2 - common
                free = mid - (divisorOf1 + divisorOf2 + common)

                tempCnt1 -= min(tempCnt1, divisorOf2)
                tempCnt2 -= min(tempCnt2, divisorOf1)
                if free >= tempCnt1 + tempCnt2:
                    ans = mid 
                    right = mid - 1
                else:
                    left = mid + 1
        return ans


