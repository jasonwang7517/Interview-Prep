"""
    You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

    The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range 
    [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

    Return the earliest year with the maximum population.
"""

class MaximumPopulationYear(object):
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