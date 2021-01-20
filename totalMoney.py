class Solution(object):
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
            