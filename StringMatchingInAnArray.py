"""
    Given an array of string words. Return all strings in words which is substring of another word in any order. 

    String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
"""

class StringMatchingInAnArray(object):
    def stringMatching(self, words):
        ans = set()
        for i in range(0, len(words) - 1):

            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    ans.add(words[i])
                elif words[j] in words[i]:
                    ans.add(words[j])
        return list(ans)
