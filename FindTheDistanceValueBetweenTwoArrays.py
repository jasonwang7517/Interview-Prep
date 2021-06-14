"""
    Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

    The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d. 
"""

class FindTheDistanceValueBetweenTwoArrays(object):
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
