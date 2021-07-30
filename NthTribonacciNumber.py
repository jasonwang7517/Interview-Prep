"""
    The Tribonacci sequence Tn is defined as follows: 

    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

    Given n, return the value of Tn.
"""

class NthTribonacciNumber(object):
    def tribonacci(self, n):
        tribs = {0 : 0, 1 : 1, 2 : 1}
        curr = 3
        while curr <= n:
            tribs[curr] = tribs[curr - 3] + tribs[curr - 2] + tribs[curr - 1]
            curr += 1
        return tribs[n]
        