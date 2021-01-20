class Solution(object):
    def sortArrayByParityII(self, A):
        odd = []
        even = []
        ans = [0] * len(A)
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(0, len(A)):
            if i % 2 == 0:
                ans[i] = even.pop()
            else:
                ans[i] = odd.pop()
        return ans
        
        