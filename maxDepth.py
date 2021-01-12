class Solution(object):
    def maxDepth(self, s):
        nestLevel = 0
        maxLevel = 0
        for ch in s:
            if ch == '(':
                nestLevel += 1
            elif ch == ')':
                if nestLevel > maxLevel:
                    maxLevel = nestLevel
                nestLevel -= 1
        return maxLevel
        