/*
    On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is 
    (0, 0), and the bottom-right cell is (n - 1, n - 1).

    A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

    Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

    The knight continues moving until it has made exactly k moves or has moved off the chessboard.

    Return the probability that the knight remains on the board after it has stopped moving.
*/

public class KnightProbabilityInChessboard {
    public double knightProbability(int N, int K, int r, int c) {
        double[][] board = new double[N][N];
        board[r][c] = 1;
        while (K > 0) {
            double[][] newBoard = new double[N][N];
            //ArrayList<ArrayList<Integer>> seen = new ArrayList<>();
            //seen.addAll();
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (board[i][j] > 0) {
                        int[][] next = getNextSquares(i, j);
                        for (int k = 0; k < next.length; k++) {
                            if (next[k][0] >= 0 && next[k][1] >= 0 && next[k][0] < N && next[k][1] < N) {
                                int row = next[k][0];
                                int col = next[k][1];
                                newBoard[row][col] += 0.125 * board[i][j];
                            }
                        }
                    }
                }
            }
            board = newBoard;
            K--;
        }
        double ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                ans += board[i][j];
            }
        }
        return ans;
    }
    
    public int[][] getNextSquares(int r, int c) {
        int[][] next = new int[8][2];
        next[0] = new int[]{r - 1, c - 2};
        next[1] = new int[]{r - 2, c - 1};
        next[2] = new int[]{r - 2, c + 1};
        next[3] = new int[]{r - 1, c + 2};
        next[4] = new int[]{r + 1, c + 2};
        next[5] = new int[]{r + 2, c + 1};
        next[6] = new int[]{r + 1, c - 2};
        next[7] = new int[]{r + 2, c - 1};
        return next;
    }
}
