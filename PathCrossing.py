"""
    Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

    Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
"""

class PathCrossing(object):
    def isPathCrossing(self, path):
        x = 0
        y = 0
        curr = (x, y)
        points = set()
        points.add(curr)
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            else:
                x -= 1
            curr = (x, y)
            if curr in points:
                return True
            points.add(curr)
        return False