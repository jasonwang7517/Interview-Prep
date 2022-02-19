"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
"""

class AddStrings(object):
    def addStrings(self, num1, num2):
        index = -1
        ans = ""
        carry = 0
        while index * -1 <= len(num1) and index * -1 <= len(num2):
            curr_sum = int(num1[index]) + int(num2[index]) + carry
            if curr_sum >= 10:
                carry = 1
            else:
                carry = 0
            ans = str(curr_sum % 10) + ans
            index -= 1
        remainder = ""
        if len(num1) > len(num2):
            index_limit = len(num1) + index
            remainder = num1[:index_limit + 1]
        elif len(num2) > len(num1):
            index_limit = len(num2) + index
            remainder = num2[:index_limit + 1]
        index = -1
        while index * -1 <= len(remainder):
            curr_sum = int(remainder[index]) + carry
            if curr_sum >= 10:
                carry = 1
            else:
                carry = 0
            ans = str(curr_sum % 10) + ans
            index -= 1
        if carry == 1:
            return "1" + ans
        return ans