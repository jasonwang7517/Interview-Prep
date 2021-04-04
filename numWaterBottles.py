class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        ans = 0
        empties = 0
        while numBottles > 0:
            ans += numBottles
            empties += numBottles
            numBottles = empties // numExchange
            empties = empties % numExchange
        return ans
