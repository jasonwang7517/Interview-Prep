"""
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.
"""

class SortArrayByParity(object):
    def sortArrayByParity(self, A):
        even = []
        odd = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            elif i % 2 == 1:
                odd.append(i)
        even.sort()
        odd.sort()
        return even + odd
        