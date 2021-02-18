class Solution(object):
    def fib(self, n):
        hm = {}
        hm[0] = 0
        hm[1] = 1
        index = 2
        while index <= n:
            hm[index] = hm[index - 1] + hm[index - 2]
            index += 1
        return hm[n]
