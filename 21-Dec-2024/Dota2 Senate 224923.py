# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        couner = Counter(senate)
        if len(couner) == 1:
            return "Radiant" if senate[0] == "R" else "Dire"
        ban_from_d = 0
        ban_from_r = 0
        while len(queue) != 1:
            turn = queue.popleft()
            if ban_from_r > 0 and turn == "R":
                ban_from_r -= 1
                couner["R"] -= 1
                if couner["R"] == 0:
                    return "Dire"
                continue
            if ban_from_d > 0 and turn == "D":
                ban_from_d -= 1
                couner["D"] -= 1
                if couner["D"] == 0:
                    return "Radiant"
                continue
            if turn == "D":
                ban_from_r += 1
            else:
                ban_from_d += 1
            queue.append(turn)
                
        return "Radiant" if queue[0] == "R" else "Dire"
            