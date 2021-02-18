class Solution(object):
    def reformatNumber(self, number):
        newString = ""
        for i in range(0, len(number)):
            if number[i] != ' ' and number[i] != '-':
                newString += number[i]

        remainder = len(newString) % 3
        ans = ""

        index = 0
        if remainder == 0:
            while index < len(newString):
                ans += newString[index:index + 3] + "-"
                index += 3
        elif remainder == 1:
            while index < len(newString) - 4:
                ans += newString[index:index + 3] + "-"
                index += 3
            ans += newString[index:index + 2] + "-"
            ans += newString[index + 2:] + "-"
        else:
            while index < len(newString) - 2:
                ans += newString[index:index + 3] + "-"
                index += 3
            ans += newString[index:] + "-"
        return ans[:-1]