"""
    Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
"""

class BinaryNumberWithAlternatingBits(object):
    def hasAlternatingBits(self, n):
        binary = bin(n)
        binary = binary[2:]
        for i in range(1, len(binary)):
            if binary[i] == binary[i - 1]:
                return False
        return True
