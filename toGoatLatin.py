class Solution(object):
    def toGoatLatin(self, S):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        words = S.split(" ")
        ans = ""

        for i in range(0, len(words)):
            word = words[i]
            if word[0] in vowels:
                word += "ma"
            elif word[0] not in vowels:
                word += word[0] + "ma"
                word = word[1:]
            numAs = i + 1
            while numAs > 0:
                word += "a"
                numAs -= 1
            ans += word + " "

        return ans[0:-1]
