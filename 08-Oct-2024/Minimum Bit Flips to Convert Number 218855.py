# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        binStart = ""
        tempS = bin(start)[2:]
        binGoal = ""
        tempG = bin(goal)[2:]
        if len(tempG) < len(tempS):
            binGoal += "0" * (len(tempS) - len(tempG)) + tempG
        else:
            binStart += "0" * (len(tempG) - len(tempS)) + tempS
        if binStart == "":
            binStart += tempS
        if binGoal == "":
            binGoal += tempG
            
        for i in range(len(binGoal)):
            ans += (binGoal[i] != binStart[i])

        return ans

