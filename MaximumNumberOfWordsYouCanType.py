"""
There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, 
return the number of words in text you can fully type using this keyboard.
"""

class MaximumNumberOfWordsYouCanType(object):
    def canBeTypedWords(self, text, brokenLetters):
        broken = set()
        ans = 0
        for i in brokenLetters:
            broken.add(i)
        words = text.split()
        for i in words:
            valid = True
            for j in i:
                if j in broken:
                    valid = False
                    break
            if valid:
                ans += 1
        return ans
        