"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
    - a, b are from arr
    - a < b
    - b - a equals to the minimum absolute difference of any two elements in arr
"""

class MinimumAbsoluteDifference(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        minDiff = 1000000
        pairs = []
        for i in range(0, len(arr) - 1):
            if (arr[i + 1] - arr[i]) < minDiff:
                minDiff = arr[i + 1] - arr[i]
                del pairs[:]
                newPair = [arr[i], arr[i + 1]]
                pairs.append(newPair)
            elif (arr[i + 1] - arr[i]) == minDiff:
                newPair = [arr[i], arr[i + 1]]
                pairs.append(newPair)
        return pairs