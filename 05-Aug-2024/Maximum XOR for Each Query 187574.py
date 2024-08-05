# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        for i in range(1, len(nums)):
            nums[i] ^= nums[i - 1]

        n = len(nums) - 1
        ans = []
        for i in range(len(nums)):
            num = bin(nums[n - i])[2:]
            temp_ans = ["0"] * maximumBit
            temp_num = "0" * (maximumBit - len(num)) + num     
            for i, bit in enumerate(temp_num):
                if bit == "0":
                    temp_ans[i] = "1"
            ans.append(int("".join(temp_ans), 2)) 
            
        return ans
    
