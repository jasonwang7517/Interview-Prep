"""
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

    - 'A': Absent.
    - 'L': Late.
    - 'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

    - The student was absent ('A') for strictly fewer than 2 days total.
    - The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.
"""

class Solution(object):
    def checkRecord(self, s):
        count_As = 0
        count_Ls = 0
        for i in s:
            if i == 'L':
                count_Ls += 1
                if count_Ls >= 3:
                    return False
            else:
                count_Ls = 0
            if i == 'A':
                count_As += 1
                if count_As >= 2:
                    return False
        return True