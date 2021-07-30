"""
    Given an integer n, add a dot (".") as the thousands separator and return it in string format.
"""

class ThousandSeparator(object):
    def thousandSeparator(self, n):
        num = str(n)
        if len(num) <= 3:
            return num
        ans = ""
        index = 0
        for i in range(len(num) - 1, -1, -1):
            ans = num[i] + ans
            index += 1
            if index == 3:
                ans = "." + ans
                index = 0
        if ans[0] == '.':
            return ans[1:]
        return ans
        