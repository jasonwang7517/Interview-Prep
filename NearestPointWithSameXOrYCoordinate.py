"""
You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). 

You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). 

A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, 
return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
"""

class NearestPointWithSameXOrYCoordinate(object):
    def nearestValidPoint(self, x, y, points):
        ans = -1
        currDist = 100000
        for i in range(0, len(points)):
            tempDist = 100000
            if points[i][0] == x and points[i][1] == y:
                return i
            if points[i][0] == x:
                tempDist = abs(y - points[i][1])
            elif points[i][1] == y:
                tempDist = abs(x - points[i][0])
            if tempDist < currDist:
                currDist = tempDist
                ans = i
        return ans