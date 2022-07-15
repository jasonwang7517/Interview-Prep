"""
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.
"""

class NumberComplement(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
        