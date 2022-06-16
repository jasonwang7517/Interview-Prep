"""
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. 
The test cases are generated such that digit occurs at least once in number.
"""

class RemoveDigitFromNumberToMaximizeResult(object):
    def removeDigit(self, number, digit):
        last_index = 0
        for i in range(len(number) - 1):
            if number[i] == digit:
                last_index = i
                if int(number[i]) < int(number[i + 1]):
                    return number[:i] + number[i + 1:]
        if number[-1] == digit:
            return number[:-1]
        return number[:last_index] + number[last_index + 1:]
                
        