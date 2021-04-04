class Solution(object):
    def findSpecialInteger(self, arr):
        toBeat = len(arr) // 4
        for i in range(0, len(arr) - toBeat):
            if arr[i] == arr[i + toBeat]:
                return arr[i]