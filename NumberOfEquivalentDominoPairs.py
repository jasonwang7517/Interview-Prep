"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one 
domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
"""

from collections import defaultdict
import math

class NumberOfEquivalentDominoPairs(object):
    def numEquivDominoPairs(self, dominoes):
        dom = defaultdict(lambda: 0)
        ans = 0
        for i in dominoes:
            i.sort()
            dom[tuple(i)] += 1
        for i in dom:
            if dom[i] > 1:
                ans += self.nCr(dom[i], 2)        
        return ans
    
    def nCr(self, n,r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)
        