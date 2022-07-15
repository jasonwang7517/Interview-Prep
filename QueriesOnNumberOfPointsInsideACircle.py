"""
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.
"""

class QueriesOnNumberOfPointsInsideACircle(object):
    def countPoints(self, points, queries):
        ans = [0 for i in range(len(queries))]
        for i in range(0, len(queries)):
            numPoints = 0
            for j in range(0, len(points)):
                if self.distance(points[j][0], queries[i][0], points[j][1], queries[i][1]) <= queries[i][2]:
                    numPoints += 1
            ans[i] = numPoints
        return ans

    def distance(self, x1, x2, y1, y2):
        return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5