"""
You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros 
are allowed in new1 and new2, and all the digits found in num must be used.
    - For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], 
    [223, 9] and [2, 329].

Return the minimum possible sum of new1 and new2.
"""

class MinimumSumOfFourDigitNumber(object):
    def minimumSum(self, num):
        ans = float('inf')
        num_string = str(num)
        possible_ints = []
        for i in range(len(num_string)):
            possible_ints.append(int(num_string[i]))
        possible_ints.sort()
        num1 = int(str(possible_ints[0]) + str(possible_ints[2]))
        num2 = int(str(possible_ints[1]) + str(possible_ints[3]))
        return num1 + num2