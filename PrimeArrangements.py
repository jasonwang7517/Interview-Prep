"""
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.
"""
import math

class PrimeArrangements(object):
    def numPrimeArrangements(self, n):
        primes = [True for i in range(n + 1)]
        p = 2
        while p ** 2 <= n:
            if primes[p]:
                for i in range(p ** 2, n + 1, p):
                    primes[i] = False
            p += 1
                
        num_primes = sum(primes[2:])
        return math.factorial(num_primes) * math.factorial(n - num_primes) % (10**9 + 7)