"""
You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.
"""

class LargestNumberAfterDigitSwapsByParity(object):
    def largestInteger(self, num):
        even = []
        odd = []
        for i in str(num):
            if int(i) % 2 == 0:
                even.append(int(i))
            else:
                odd.append(int(i))
        even.sort(reverse = True)
        odd.sort(reverse = True)
        ans = ""
        for i in str(num):
            if int(i) % 2 == 0:
                ans += str(even.pop(0))
            else:
                ans += str(odd.pop(0))
        return int(ans)
        