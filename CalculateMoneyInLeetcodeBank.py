"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will 
put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
"""

class CalculateMoneyInLeetcodeBank(object):
    def totalMoney(self, n):
        day = 1
        week = [1, 2, 3, 4, 5, 6, 7]
        index = 0
        ans = 0
        while day <= n:
            ans += week[index]
            day += 1
            week[index] += 1
            if index <  6:
                index += 1
            else:
                index = 0
        return ans
            