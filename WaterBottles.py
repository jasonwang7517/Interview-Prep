"""
    Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

    The operation of drinking a full water bottle turns it into an empty bottle.

    Return the maximum number of water bottles you can drink.
"""

class WaterBottles(object):
    def numWaterBottles(self, numBottles, numExchange):
        ans = 0
        empties = 0
        while numBottles > 0:
            ans += numBottles
            empties += numBottles
            numBottles = empties // numExchange
            empties = empties % numExchange
        return ans
