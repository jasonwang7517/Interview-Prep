class Solution(object):
    def sortArrayByParity(self, A):
        even = []
        odd = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            elif i % 2 == 1:
                odd.append(i)
        even.sort()
        odd.sort()
        return even + odd
        