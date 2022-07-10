"""
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.
"""

class ValidBoomerang(object):
    def isBoomerang(self, points):
        for i in range(2):
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    return False
        return not self.checkIfStraightLine(points)
        
        
    def checkIfStraightLine(self, points):
        (x0, y0) = points[0]
        (x1, y1) = points[1]
        for i in points:
            if (x1 - x0) * (i[1] - y1) != (i[0] - x1) * (y1 - y0):
                return False
        return True
        