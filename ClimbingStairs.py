"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class ClimbingStairs(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        n_1 = 2
        n_2 = 1
        ans = 0
        for i in range(3, n + 1):
            ans = n_1 + n_2
            n_2 = n_1
            n_1 = ans
        return ans
        