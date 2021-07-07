"""
    Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.

    Return a list of two integers [A, B] where:
    - A and B are No-Zero integers.
    - A + B = n

    It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.
"""

class ConvertIntegerToTheSumOfTwoNoZeroIntegers(object):
    def getNoZeroIntegers(self, n):
        ans = [0, 0]
        for i in range(1, (n // 2) + 1):
            elem1 = True
            elem2 = True
            for j in str(i):
                if j == '0':
                    elem1 = False
                    break
            if elem1:
                for k in str(n - i):
                    if k == '0':
                        elem2 = False
                        break
            if elem1 and elem2:
                ans[0] = i
                ans[1] = n - i
                return ans