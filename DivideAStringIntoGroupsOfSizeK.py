"""
A string s can be partitioned into groups of size k using the following procedure:

    The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each character can be a part of exactly one group.
    For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.

Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.

Given the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.
"""

class DivideAStringIntoGroupsOfSizeK(object):
    def divideString(self, s, k, fill):
        ans = []
        index = 0
        while index < len(s) - k:
            ans.append(s[index : index + k])
            index += k
        final_word = ""
        if index < len(s):
            while index < len(s):
                final_word += s[index]
                index += 1
            for i in range(k - len(final_word)):
                final_word += fill
            ans.append(final_word)
        return ans
        