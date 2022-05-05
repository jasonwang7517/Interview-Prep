"""
You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.
"""

class MinimumNumberOfOperationsToConvertTime(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        ans = 0
        current_minutes = (int(current[:2]) * 60) + int(current[3:])
        correct_minutes = (int(correct[:2]) * 60) + int(correct[3:])
        diff = correct_minutes - current_minutes
        while diff >= 5:
            ans += 1
            if diff >= 60:
                diff -= 60
            elif diff >= 15:
                diff -= 15
            else:
                diff -= 5
        return ans + diff