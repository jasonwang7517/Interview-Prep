"""
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + 
arr[j + 1] + ... + arr[arr.length - 1])
"""

class PartitionArrayIntoThreePartsWithEqualSum(object):
    def canThreePartsEqualSum(self, arr):
        if sum(arr) % 3 != 0:
            return False
        target = sum(arr) / 3
        curr_sum = 0
        subarrays = 0
        for i in arr:
            curr_sum += i
            if curr_sum == target:
                subarrays += 1
                curr_sum = 0
        return subarrays >= 3
        