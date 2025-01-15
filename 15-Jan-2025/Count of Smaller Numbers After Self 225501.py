# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        new = []
        for i in range(len(nums)):
            new.append((nums[i], i))
            

        def merge(left_hand, right_hand):
            left = 0
            right = 0
            while left < len(left_hand)  and right < len(right_hand):
                if left_hand[left][0] > right_hand[right][0]:
                    right += 1
                else:
                    ans[left_hand[left][1]] += right
                    left += 1
       
            while left < len(left_hand):
                ans[left_hand[left][1]] += right
                left += 1

            left = right = 0
            res = []
            while left < len(left_hand) or right < len(right_hand):
                if right == len(right_hand) or left < len(left_hand) and left_hand[left][0] <= right_hand[right][0]:
                    res.append(left_hand[left])
                    left += 1
                else:
                    res.append(right_hand[right])
                    right += 1
            
            return res


        def mergeSort(left, right, arr):
            if left >= right:
                return [arr[left]]

            mid = left + (right - left) // 2

            left_hand = mergeSort(left, mid, arr)
            right_hand = mergeSort(mid + 1, right, arr)

            return merge(left_hand, right_hand)

        mergeSort(0, len(new) - 1, new)
        return ans