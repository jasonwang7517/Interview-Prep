"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
"""

class MaximumNumberOfWordsInSentence(object):
    def mostWordsFound(self, sentences):
        ans = 0
        for i in sentences:
            curr_length = len(i.split(' '))
            ans = max(ans, curr_length)
        return ans
        