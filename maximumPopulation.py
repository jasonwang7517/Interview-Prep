class Solution(object):
    def maximumPopulation(self, logs):
        years = [0] * 2051
        for i in logs:
            years[i[0]] += 1
            years[i[1]] -= 1
        currPop = 0
        maxPop = 0
        ans = 1950
        for i in range(1950, 2051):
            currPop += years[i]
            if currPop > maxPop:
                ans = i
                maxPop = currPop
        return ans