"""
    Given a date string in the form Day Month Year, where:
    - Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
    - Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
    - Year is in the range [1900, 2100].
    
    Convert the date string to the format YYYY-MM-DD, where:
    - YYYY denotes the 4 digit year.
    - MM denotes the 2 digit month.
    - DD denotes the 2 digit day.
"""

class ReformatDate(object):
    def reformatDate(self, date):
        dateInfo = date.split(" ")
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
                  "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day = dateInfo[0][:len(dateInfo[0]) - 2]
        if len(day) == 1:
            day = "0" + day
        ans = dateInfo[2] + "-" + months[dateInfo[1]] + "-" + day
        return ans
