"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.
"""

class FindTicTacToeWinner(object):
    def tictactoe(self, moves):
        grid = [[0 for i in range(3)] for j in range(3)]
        x_move = True
        current_character = 'X'
        character_map = {'X' : 'A', 'O' : 'B'}
        for i in moves:
            if x_move:
                current_character = 'X'
            else:
                current_character = 'O'
            grid[i[0]][i[1]] = current_character
            for i in range(3):
                if (grid[i][0] == current_character and grid[i][1] == current_character and grid[i][2] == current_character) or (grid[0][i] == current_character and grid[1][i] == current_character and grid[2][i] == current_character):
                    return character_map[current_character]
            if (grid[0][0] == current_character and grid[1][1] == current_character and grid[2][2] == current_character) or (grid[0][2] == current_character and grid[1][1] == current_character and grid[2][0] == current_character):
                return character_map[current_character]
            x_move = not x_move
        if len(moves) < 9:
            return "Pending"
        return "Draw"