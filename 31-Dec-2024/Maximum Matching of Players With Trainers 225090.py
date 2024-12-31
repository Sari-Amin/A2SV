# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        left = right = 0
        res = 0
        while left < len(players) and right < len(trainers):
            if players[left] <= trainers[right]:
                res += 1
                left += 1
                right += 1
            else:
                right += 1
        return res