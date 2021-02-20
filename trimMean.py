class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        bound = int(len(arr) * 0.05)
        newArr = arr[bound:bound * -1]
        return float(sum(newArr)) / len(newArr)
