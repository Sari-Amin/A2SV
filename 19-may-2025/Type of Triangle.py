class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c = nums
        if a < c + b and b < a + c and c < a + b:
            if a == b == c:
                return "equilateral"
            elif a == b or b == c or a == c:
                return "isosceles"
            return "scalene"
        return "none"
