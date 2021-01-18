class Solution(object):
    def countGoodRectangles(self, rectangles):
        ans = 0
        currMax = 0
        for i in range(0, len(rectangles)):
            currLen = min(rectangles[i][0], rectangles[i][1])
            if currLen == currMax:
                ans += 1
            elif currLen > currMax:
                currMax = currLen
                ans = 1
        return ans
        