class Solution(object):
    def sumBase(self, n, k):
        ans = 0
        while n > 0:
            ans += n % k
            n //= k
        return ans