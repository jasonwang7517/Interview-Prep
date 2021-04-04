class Solution(object):
    def reformatDate(self, date):
        dateInfo = date.split(" ")
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
                  "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day = dateInfo[0][:len(dateInfo[0]) - 2]
        if len(day) == 1:
            day = "0" + day
        ans = dateInfo[2] + "-" + months[dateInfo[1]] + "-" + day
        return ans
