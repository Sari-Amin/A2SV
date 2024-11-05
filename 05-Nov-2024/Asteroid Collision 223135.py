# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for asteroid in asteroids:
            while res and res[-1] > 0 and asteroid < 0:
                diff = res[-1] + asteroid
                if diff > 0:
                    asteroid = 0
                elif diff < 0:
                    res.pop()
                else:
                    asteroid = 0
                    res.pop()
            if asteroid:
                res.append(asteroid)
            
        return res