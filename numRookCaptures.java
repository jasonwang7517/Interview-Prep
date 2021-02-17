public class numRookCaptures {
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
