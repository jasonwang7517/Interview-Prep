class Solution(object):
    def distributeCandies(self, candyType):
        counts = set(candyType)
        return min(len(candyType) / 2, len(counts))