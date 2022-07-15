"""
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:
    - Rank is an integer starting from 1.
    - The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
    - Rank should be as small as possible.
"""

class RankTransformOfAnArray(object):
    def arrayRankTransform(self, arr):
        if len(arr) == 0:
            return []
        newArr = [0 for i in range(0, len(arr))]
        for i in range(0, len(arr)):
            newArr[i] = arr[i]
        newArr.sort()
        ranks = {}
        currRank = 1
        ranks[newArr[0]] = currRank
        currRank += 1
        for i in range(1, len(newArr)):
            if newArr[i] != newArr[i - 1]:
                ranks[newArr[i]] = currRank
                currRank += 1
        ans = [0 for i in range(0, len(arr))]
        for i in range(0, len(arr)):
            ans[i] = ranks[arr[i]]
        return ans
        