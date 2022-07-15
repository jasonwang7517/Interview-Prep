"""
Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third 
comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".
"""

class OccurrencesAfterBigram(object):
    def findOcurrences(self, text, first, second):
        words = text.split(" ")
        ans = []
        for i in range(0, len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                ans.append(words[i + 2])
                i += 2
        return ans
