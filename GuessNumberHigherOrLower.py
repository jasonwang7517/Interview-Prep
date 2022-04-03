"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

    - -1: Your guess is higher than the number I picked (i.e. num > pick).
    - 1: Your guess is lower than the number I picked (i.e. num < pick).
    - 0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

class Solution(object):

    def guess(num):
        return -1

    def guessNumber(self, n):
        current_max = n
        current_min = 1
        current_guess = self.average(current_max, current_min)
        while self.guess(current_guess) != 0 and current_max - current_min >= 2:
            if self.guess(current_guess) == -1:
                current_max = current_guess
            elif self.guess(current_guess) == 1:
                current_min = current_guess
            current_guess = self.average(current_max, current_min)
        if self.guess(current_guess) == 0:
            return current_guess
        if self.guess(current_max) != 0:
            return current_min
        return current_max
    
    def average(self, n1, n2):
        return (n1 + n2) // 2