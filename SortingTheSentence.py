"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
    - For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".

Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
"""

class SortingTheSentence(object):
    def sortSentence(self, s):
        words = s.split(" ")
        sentence = [0] * len(words)
        for w in words:
            index = int(w[-1]) - 1
            sentence[index] = w[:-1]
        ans = ""
        for i in sentence:
            ans += i + " "
        return ans[:-1]