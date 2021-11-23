"""
There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.
"""

class TwoFurthestHousesWithDifferentColors(object):
    def maxDistance(self, colors):
        left = {}
        right = {}
        for i in range(0, len(colors)):
            if colors[i] not in left:
                left[colors[i]] = i
            else:
                right[colors[i]] = i
        ans = 0
        for i in left:
            for j in right:
                if abs(left[i] - right[j]) > ans and i != j:
                    ans = abs(left[i] - right[j])
        ans = max(ans, (max(left.values()) - min(left.values())))                    
        return ans
        