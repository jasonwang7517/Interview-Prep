"""
    x is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose 
    to leave it alone.

    A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different 
    direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

    Now given a positive number n, how many numbers x from 1 to n are good?
"""

class RotatedDigits(object):
    def rotatedDigits(self, n):
        rotate = {'0' : '0', '1' : '1', '8' : '8', '2' : '5', '5' : '2', '6' : '9', '9' : '6'}
        ans = 0
        for i in range(1, n + 1):
            currNum = str(i)
            rotated = ""
            for j in currNum:
                if j not in rotate:
                    break
                else:
                    rotated += rotate[j]
            if rotated != currNum and len(rotated) == len(currNum):
                ans += 1
        return ans
        