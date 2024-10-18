# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        team = set()
        res = [[], []]
      
        lose = defaultdict(int)

        for w,l in matches:
            lose[l] += 1
            team.add(w)
            team.add(l)
        for i in team:
            if lose[i] == 0:
                res[0].append(i)
            if lose[i] == 1:
                res[1].append(i)

        return [sorted(res[0]), sorted(res[1])]
        

            