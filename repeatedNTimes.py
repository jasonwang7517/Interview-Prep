class Solution(object):
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
        