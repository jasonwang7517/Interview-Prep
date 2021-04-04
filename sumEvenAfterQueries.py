class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        ans = 0
        ansArray = []
        for i in A:
            if i % 2 == 0:
                ans += i
        for q in queries:
            index = q[1]
            newVal = A[index] + q[0]
            if newVal % 2 == 0:
                if A[index] % 2 == 0:
                    ans += q[0]
                elif A[index] % 2 == 1:
                    ans += newVal
            elif A[index] % 2 == 0 and newVal % 2 == 1:
                ans -= A[index]
            A[index] = newVal
            ansArray.append(ans)
        return ansArray