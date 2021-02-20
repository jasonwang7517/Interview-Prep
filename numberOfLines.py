class Solution(object):
    def numberOfLines(self, widths, s):
        lines = 1
        currWidth = 0
        for i in range(0, len(s)):
            toAdd = widths[ord(s[i]) - ord('a')]
            if currWidth + toAdd > 100:
                lines += 1
                currWidth = toAdd
            else:
                currWidth += toAdd
        ans = [lines, currWidth]
        return ans
