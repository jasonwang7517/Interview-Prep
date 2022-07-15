"""
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, 
"xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.
"""

class PositionsOfLargeGroups(object):
    def largeGroupPositions(self, s):
        groups = []
        pointer_left = 0
        for pointer_right in range(len(s)):
            if pointer_right == len(s) - 1 or s[pointer_right] != s[pointer_right + 1]:
                if pointer_right - pointer_left >= 2:
                    groups.append([pointer_left, pointer_right])
                pointer_left = pointer_right + 1
        return groups