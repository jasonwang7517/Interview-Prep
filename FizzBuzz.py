"""
Given an integer n, return a string array answer (1-indexed) where:
    - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    - answer[i] == "Fizz" if i is divisible by 3.
    - answer[i] == "Buzz" if i is divisible by 5.
    - answer[i] == i if non of the above conditions are true.
"""

class FizzBuzz(object):
    def fizzBuzz(self, n):
        ans = []
        for i in range(0, n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                ans.append("FizzBuzz")
            elif (i + 1) % 3 == 0:
                ans.append("Fizz")
            elif (i + 1) % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(i + 1)
        return ans