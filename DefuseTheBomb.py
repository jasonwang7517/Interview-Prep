"""
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
    - If k > 0, replace the ith number with the sum of the next k numbers.
    - If k < 0, replace the ith number with the sum of the previous k numbers.
    - If k == 0, replace the ith number with 0.
    - As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
"""

class DefuseTheBomb(object):
    def decrypt(self, code, k):
        n = len(code)
        res = [0] * n
        if k > 0:
            res[0] = sum(code[1 : k + 1])
            for i in range(1, n):
                res[i] = res[i - 1] + code[(i + k) % n] - code[i]
        elif k < 0:
            res[0] = sum(code[n + k : n])
            for i in range(1, n):
                res[i] = res[i - 1] + code[i - 1] - code[(n + k + i - 1) % n]
        return res