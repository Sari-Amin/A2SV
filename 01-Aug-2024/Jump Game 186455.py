# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        position = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= position:
                position =  i 
                
        return position == 0
