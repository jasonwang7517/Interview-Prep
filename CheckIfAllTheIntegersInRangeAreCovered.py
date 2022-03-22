"""
You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.
"""

class CheckIfAllIntegersInRangeAreCovered(object):
    def isCovered(self, ranges, left, right):
        for i in range(left, right + 1):
            covered = False
            for j in ranges:
                if j[0] <= i and j[1] >= i:
                    covered = True
                    break
            if not covered:
                return False
        return True
        