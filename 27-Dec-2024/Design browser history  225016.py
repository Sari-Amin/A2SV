# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:

        while len(self.history) > self.curr + 1:
            self.history.pop()
        self.history.append(url)
        self.curr += 1
        

    def back(self, steps: int) -> str:
        if steps > self.curr:
            self.curr = 0
        else:
            self.curr -= steps
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        if steps + self.curr >= len(self.history):
            self.curr = len(self.history) - 1
        else:
            self.curr += steps
        return self.history[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)