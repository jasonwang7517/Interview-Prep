"""
You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.
"""

class LatestTimeByReplacingHiddenDigits(object):
    def maximumTime(self, time):
        numbers = []
        for i in time:
            numbers.append(str(i))
        if numbers[0] == '?':
            if numbers[1] != '?' and numbers[1] >= '4':
                numbers[0] = '1'
            else:
                numbers[0] = '2'
        if numbers[1] == '?':
            if numbers[0] == '2':
                numbers[1] = '3'
            else:
                numbers[1] = '9'
        if numbers[3] == '?':
            numbers[3] = '5'
        if numbers[4] == '?':
            numbers[4] = '9'
        return ''.join(numbers)
        