"""
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
"""

class CountCommonWordsWithOneOccurrence(object):
    def countWords(self, words1, words2):
        counts1 = {}
        for word in words1:
            if word not in counts1:
                counts1[word] = 1
            else:
                counts1[word] += 1
        counts2 = {}
        for word in words2:
            if word not in counts2:
                counts2[word] = 1
            else:
                counts2[word] += 1
        ans = 0
        for i in counts1:
            if counts1[i] == 1 and i in counts2 and counts2[i] == 1:
                ans += 1
        return ans
        