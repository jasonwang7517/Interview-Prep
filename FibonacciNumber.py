"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
starting from 0 and 1. That is,
    - F(0) = 0, F(1) = 1
    - F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
"""

class FibonacciNumber(object):
    def fib(self, n):
        hm = {}
        hm[0] = 0
        hm[1] = 1
        index = 2
        while index <= n:
            hm[index] = hm[index - 1] + hm[index - 2]
            index += 1
        return hm[n]
