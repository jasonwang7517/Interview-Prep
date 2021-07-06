"""
    Given a string licensePlate and an array of strings words, find the shortest completing word in words.

    A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter 
    appears more than once in licensePlate, then it must appear in the word the same number of times or more.

    For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

    Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.
"""

class ShortestCompletingWord(object):
    def shortestCompletingWord(self, licensePlate, words):
        ans = "aaaaaaaaaaaaaaaa"
        letters = {}
        for i in licensePlate:
            if ord(i.lower()) >= 97 and ord(i.lower()) <= 122:
                if i.lower() in letters:
                    letters[i.lower()] += 1
                else:
                    letters[i.lower()] = 1
        for i in words:
            changeAns = True
            letters2 = {}
            for j in i:
                if j in letters2:
                    letters2[j] += 1
                else:
                    letters2[j] = 1
            for k in letters:
                if k not in letters2 or letters[k] > letters2[k]:
                    changeAns = False
                    break
            if changeAns:
                if len(i) < len(ans):
                    ans = i
                    print(ans)
        return ans