"""
    Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
"""

class ExcelSheetColumnNumber(object):
    def titleToNumber(self, columnTitle):
        total = 0
        exp = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            total += (26 ** exp) * (ord(columnTitle[i]) - ord('A') + 1)
            exp += 1
        return total