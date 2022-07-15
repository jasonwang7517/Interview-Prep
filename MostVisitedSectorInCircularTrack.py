"""
Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1 to n. 

A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector rounds[i - 1] and ends at sector rounds[i]. 
    - For example, round 1 starts at sector rounds[0] and ends at sector rounds[1].

Return an array of the most visited sectors sorted in ascending order.

Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).
"""

class MostVisitedSectorInACircularTrack(object):
    def mostVisited(self, n, rounds):
        sectors = {}
        currMax = 0
        for i in range(1, n + 1):
            sectors[i] = 0
        for i in range(0, len(rounds) - 1):
            if rounds[i] < rounds[i + 1]:
                for j in range(rounds[i] + 1, rounds[i + 1] + 1):
                    sectors[j] += 1
                    if sectors[j] > currMax:
                        currMax = sectors[j]
            else:
                for j in range(rounds[i] + 1, n + 1):
                    sectors[j] += 1
                    if sectors[j] > currMax:
                        currMax = sectors[j]
                for j in range(1, rounds[i + 1] + 1):
                    sectors[j] += 1
                    if sectors[j] > currMax:
                        currMax = sectors[j]
        sectors[rounds[0]] += 1
        if sectors[rounds[0]] > currMax:
            currMax = sectors[rounds[0]]
        final = []
        for i in sectors:
            if sectors[i] == currMax:
                final.append(i)
        return final
        