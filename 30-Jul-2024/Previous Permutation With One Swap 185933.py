# Problem: Previous Permutation With One Swap - https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        ind1 = 0
        ind2 = 0
        for i in range(len(arr) - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                ind1 = i - 1
                break
  
        curr = 0
        for i in range(ind1 + 1, len(arr)):
            if arr[i] > curr and arr[i] < arr[ind1]:
                ind2 = i
                curr = arr[i]
     
        arr[ind1], arr[ind2] = arr[ind2], arr[ind1]
        return arr