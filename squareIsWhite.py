class Solution(object):
    def squareIsWhite(self, coordinates):
        oddCols = {'a', 'c', 'e', 'g'}
        evenCols = {'b', 'd', 'f', 'h'}
        column = coordinates[0]
        row = int(coordinates[1])
        if ((column in oddCols and row % 2 == 1) or (column in evenCols and row % 2 == 0)):
            return False
        else:
            return True
