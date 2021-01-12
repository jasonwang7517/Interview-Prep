class Solution(object):
    def finalPrices(self, prices):
        ans = [0] * len(prices)
        for i in range(0, len(prices)):
            ans[i] = prices[i]
            for j in range (i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    ans[i] = prices[i] - prices[j]
                    break
        return ans
        