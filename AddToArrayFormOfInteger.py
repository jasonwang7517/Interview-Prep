"""
The array-form of an integer num is an array representing its digits in left to right order.
    - For example, for num = 1321, the array form is [1,3,2,1].

Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
"""

class AddToArrayFormOfInteger(object):
    def addToArrayForm(self, num, k):
        ans = ""
        for i in num:
            ans += str(i)
        ans = str(int(''.join(ans)) + k)
        final_ans = []
        for i in ans:
            final_ans.append(int(i))
        return final_ans