"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant 
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class PlusOne(object):
    def plusOne(self, digits):
        index = len(digits) - 1
        carry = False
        digits[index] += 1
        while index >= 0:
            if carry:
                digits[index] += 1
                carry = False
            if digits[index] <= 9:
                return digits
            else:
                digits[index] = digits[index] % 10
                carry = True
                index -= 1
        digits.insert(0, 1)
        return digits