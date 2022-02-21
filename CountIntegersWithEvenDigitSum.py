"""
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.
"""

class CountIntegersWithEvenDigitSum(object):
    def countEven(self, num):
        ans = 0
        for i in range(1, num + 1):
            num = str(i)
            curr_sum = 0
            for char in num:
                curr_sum += int(char)
            if curr_sum % 2 == 0:
                ans += 1
        return ans
        