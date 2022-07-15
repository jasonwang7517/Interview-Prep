"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
"""

class HammingDistance(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')
        