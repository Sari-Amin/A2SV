# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefixSum = [0 for i in range(len(s))]
        for shift in shifts:
            if shift[2] == 1:
                prefixSum[shift[0]] += 1
                if shift[1] + 1 < len(s):
                    prefixSum[shift[1]+1] -= 1
            else:
                prefixSum[shift[0]] -= 1
                if shift[1] + 1 < len(s):
                    prefixSum[shift[1]+1] += 1
        ans = ""
        for i in range(len(prefixSum)):
            if i != 0:
                prefixSum[i] += prefixSum[i-1]
            ans += chr((ord(s[i]) - ord('a') + prefixSum[i]) % 26 + ord('a'))
            
        return ans