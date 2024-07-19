# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        ans = 0 
        def merge(left_hand, right_hand):
            nonlocal ans
            left = right = 0
            while left < len(left_hand) and right < len(right_hand):
                if left_hand[left] <= diff + right_hand[right]:
                    ans += len(right_hand) - right
                    left += 1
                else:
                    right += 1
    
            left = right = 0
            res = []
            while left < len(left_hand) or right < len(right_hand):
                if right == len(right_hand) or left < len(left_hand) and left_hand[left] <= right_hand[right]:
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
        n_nums = []
        for i in range(len(nums1)):
            n_nums.append(nums1[i] - nums2[i])
        temp = mergeSort(0, len(n_nums) - 1, n_nums)
        return ans