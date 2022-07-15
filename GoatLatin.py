"""
A sentence sentence is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:
    - If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
    - For example, the word 'apple' becomes 'applema'.
    - If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
    - For example, the word "goat" becomes "oatgma".

    - Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
    - For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

Return the final sentence representing the conversion from sentence to Goat Latin. 
"""
class GoatLatin(object):
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
