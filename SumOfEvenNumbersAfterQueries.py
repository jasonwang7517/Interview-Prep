"""
    We have an array nums of integers, and an array queries of queries.

    For the i-th query val = queries[i][0], index = queries[i][1], we add val to nums[index].  Then, the answer to the i-th query is the sum of the even values of A.

    (Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array nums.)

    Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.
"""

class SumOfEvenNumbersAfterQueries(object):
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