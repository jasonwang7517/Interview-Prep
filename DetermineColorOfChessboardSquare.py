"""
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.
"""

class DetermineColorOfChessboardSquare(object):
    def squareIsWhite(self, coordinates):
        oddCols = {'a', 'c', 'e', 'g'}
        evenCols = {'b', 'd', 'f', 'h'}
        column = coordinates[0]
        row = int(coordinates[1])
        if ((column in oddCols and row % 2 == 1) or (column in evenCols and row % 2 == 0)):
            return False
        else:
            return True
