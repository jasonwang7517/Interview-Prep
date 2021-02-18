class Solution(object):
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