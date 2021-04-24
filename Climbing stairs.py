class Solution:
    def __init__(self):
        self.step = {}
        
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if (n in self.step):
            return self.step[n]
        self.step[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.step[n]