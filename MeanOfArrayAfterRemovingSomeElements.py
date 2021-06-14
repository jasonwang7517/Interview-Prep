"""
    Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

    Answers within 10-5 of the actual answer will be considered accepted.
"""

class MeanOfArrayAfterRemovingSomeElements(object):
    def trimMean(self, arr):
        arr.sort()
        bound = int(len(arr) * 0.05)
        newArr = arr[bound:bound * -1]
        return float(sum(newArr)) / len(newArr)
