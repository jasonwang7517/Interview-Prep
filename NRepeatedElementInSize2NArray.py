"""
In a array nums of size 2 * n, there are n + 1 unique elements, and exactly one of these elements is repeated n times.

Return the element repeated n times.
"""

class NRepeatedElementInSize2NArray(object):
    def repeatedNTimes(self, A):
        target = len(A) / 2
        map = {}
        for el in A:
            if el in map:
                map[el] = map[el] + 1
                if map[el] == target:
                    return el
            else:
                map[el] = 1
        