"""
    A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

    Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
"""

class CountSquareSumTriples(object):
    def countTriples(self, n):
        ans = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                square = (i ** 2) + (j ** 2)
                root = int(square ** 0.5)
                if root ** 2 == square and root <= n:
                    ans += 2
        return ans
        