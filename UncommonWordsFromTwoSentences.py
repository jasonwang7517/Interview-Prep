"""
    A sentence is a string of single-space separated words where each word consists only of lowercase letters.

    A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

    Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
"""

class UncommonWordsFromTwoSentences(object):
    def uncommonFromSentences(self, A, B):
        dict ={}
        ans = []
        for s in A.split(" "):
            if s not in dict:
                dict[s] = 1
            else:
                dict[s] = dict[s] + 1
        for s in B.split(" "):
            if s not in dict:
                dict[s] = 1
            else:
                dict[s] = dict[s] + 1
        for s in dict:
            if dict[s] == 1:
                ans.append(s)
        return ans