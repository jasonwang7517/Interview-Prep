class Solution(object):
    def largestAltitude(self, gain):
        alt = 0
        highest = 0
        for i in gain:
            alt += i
            if alt > highest:
                highest = alt
        return max(0, highest)
        