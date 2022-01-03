"""
There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.

You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:

    The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
    The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').

For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.

Return the number of rods that have all three colors of rings on them.
"""

class RingsAndRods(object):
    def countPoints(self, rings):
        red = [0 for i in range(10)]
        blue = [0 for i in range(10)]
        green = [0 for i in range(10)]
        i = 0
        while i < len(rings) - 1:
            current_color = rings[i]
            ring = int(rings[i + 1])
            if current_color == 'R':
                red[ring] += 1
            elif current_color == 'G':
                green[ring] += 1
            else:
                blue[ring] += 1
            i += 2 
        ans = 0
        for i in range(10):
            if red[i] > 0 and blue[i] > 0 and green[i] > 0:
                ans += 1
        return ans