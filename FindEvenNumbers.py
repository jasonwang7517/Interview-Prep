"""
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:
    - The integer consists of the concatenation of three elements from digits in any arbitrary order.
    - The integer does not have leading zeros.
    - The integer is even.

For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.
"""
from itertools import permutations

class Find3DigitEvenNumbers(object):
    def findEvenNumbers(self, digits):
        ans = set()
        for x, y, z in permutations(digits, 3):
            if x != 0 and z % 2 == 0:
                ans.add(100 * x + 10 * y + z)
        return sorted(ans)