class Solution(object):
    def distributeCandies(self, candies, num_people):
        index = 0
        nextAmount = 1
        ans = [0] * num_people
        while candies > 0:
            if candies < nextAmount:
                ans[index] += candies
                return ans
            ans[index] += nextAmount
            candies -= nextAmount
            nextAmount += 1
            index += 1
            if index >= len(ans):
                index = 0
        return ans