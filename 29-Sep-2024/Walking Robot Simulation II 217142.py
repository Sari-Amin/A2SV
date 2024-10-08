# Problem: Walking Robot Simulation II - https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot:

    def __init__(self, width: int, height: int):
        self.pos = 0
        self.dir = 0
        self.dirs = {0: "East", 1: "North", 2: "West", 3: "South"}
        self.width = width - 1
        self.height = height - 1
        self.mid = height + width - 2

    def step(self, steps: int) -> None:
        self.pos += steps
        self.pos %= (self.mid * 2)
        if self.pos > self.mid + self.width:
            self.dir = 3
        elif self.pos > self.mid:
            self.dir = 2
        elif self.pos > self.width:
            self.dir = 1
        elif not self.pos:
            self.dir = 3
        else:
            self.dir = 0

    def getPos(self) -> List[int]:
        if self.pos > self.mid + self.width:
            return [0,self.height - (self.pos - self.mid - self.width)]
        elif self.pos > self.mid:
            return [self.width - (self.pos - self.mid) ,self.height]
        elif self.pos > self.width:
            return [self.width, self.pos - self.width ]
        else:
            return [self.pos,0]

    def getDir(self) -> str:
        return self.dirs[self.dir]
        

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(steps)
# param_2 = obj.getPos()
# param_3 = obj.getDir()