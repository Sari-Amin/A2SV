# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        sortedarr = sorted(arr)
        if arr == sortedarr:
            return res
        r = len(arr)
        while arr != sortedarr:
            temp = arr.index(max(arr[:r])) + 1
            res.append(temp)
            arr[:temp] = arr[:temp][::-1]
            arr[:r] = arr[:r][::-1]
            res.append(r)
            r -= 1
        return res