"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the 
flowerbed without violating the no-adjacent-flowers rule.
"""

class CanPlaceFlowers(object):
    def canPlaceFlowers(self, flowerbed, n):
        index = 1
        ans = 0
        if len(flowerbed) == 1:
            return (sum(flowerbed) == 0 and n <= 1) or n == 0
        if len(flowerbed) == 2:
            return (sum(flowerbed) == 0 and n <= 1) or n == 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            ans += 1
            flowerbed[0] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            ans += 1
        while index < len(flowerbed) - 1:
            if flowerbed[index - 1] + flowerbed[index] + flowerbed[index + 1] == 0:
                flowerbed[index] = 1
                ans += 1
            else:
                index += 1
        return ans >= n
        