/*
    On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

    When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of 
    the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number 
    of available captures for the white rook is the number of pawns that the rook is attacking.

    Return the number of available captures for the white rook.
*/

public class AvailableCapturesForRook {
    public int numRookCaptures(char[][] board) {
        int row = 0;
        int col = 0;
        int ans = 0;
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 'R') {
                    row = i;
                    col = j;
                    break;
                }
            }
        }
        
        for (int j = col; j >= 0; j--) {
            if (board[row][j] == 'p') {
                ans += 1;
                break;
            }
            else if (board[row][j] == 'B') {
                break;
            }
        }
        
        for (int j = col; j < board[0].length; j++) {
            if (board[row][j] == 'p') {
                ans += 1;
                break;
            }
            else if (board[row][j] == 'B') {
                break;
            }
        }
        
        for (int i = row; i >= 0; i--) {
            if (board[i][col] == 'p') {
                ans += 1;
                break;
            }
            else if (board[i][col] == 'B') {
                break;
            }
        }
        
        for (int i = row; i < board.length; i++) {
            if (board[i][col] == 'p') {
                ans += 1;
                break;
            }
            else if (board[i][col] == 'B') {
                break;
            }
        }
        return ans;
    }
}
