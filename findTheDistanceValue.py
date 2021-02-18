class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        ans = 0
        for i in range(0, len(arr1)):
            iterate = True
            for j in range(0, len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    iterate = False
                    break
            if iterate:
                ans += 1
        return ans
