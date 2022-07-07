"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that:
    - i != j
    - 0 <= i, j < arr.length
    - arr[i] == 2 * arr[j]
"""

class CheckIfNAndItsDoubleExist(object):
    def checkIfExist(self, arr):
        nums = set(arr)
        num_zeroes = 0
        for i in arr:
            if i == 0:
                num_zeroes += 1
        if num_zeroes >= 2:
            return True
        for i in nums:
            if i != 0 and 2 * i in nums:
                return True
        return False
        