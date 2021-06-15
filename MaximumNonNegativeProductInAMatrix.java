/*
    You are given a rows x cols matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

    Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (rows - 1, cols - 1), find the path with the maximum 
    non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

    Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative return -1.

    Notice that the modulo is performed after getting the maximum product.
*/

public class MaximumNonNegativeProductInAMatrix {
    public int maxProductPath(int[][] grid) {
        long[][][] maxPath = new long[grid.length][grid[0].length][2];
        maxPath[0][0][0] = grid[0][0];
        maxPath[0][0][1] = grid[0][0];
        for (int i = 1; i < grid.length; i++) {
            maxPath[i][0][0] = maxPath[i - 1][0][0] * grid[i][0];
            maxPath[i][0][1] = maxPath[i - 1][0][1] * grid[i][0];
        }
        for (int i = 1; i < grid[0].length; i++) {
            maxPath[0][i][0] = maxPath[0][i - 1][0] * grid[0][i];
            maxPath[0][i][1] = maxPath[0][i - 1][1] * grid[0][i];
        }
        for (int i = 1; i < grid.length; i++) {
            for (int j = 1; j < grid[0].length; j++) {
                int currElement = grid[i][j];
                long a = maxPath[i - 1][j][1] * currElement;
                long b = maxPath[i - 1][j][0] * currElement;
                long c = maxPath[i][j - 1][0] * currElement;
                long d = maxPath[i][j - 1][1] * currElement;
                maxPath[i][j][0] = Math.min(a, Math.min(b, Math.min(c, d)));
                maxPath[i][j][1] = Math.max(a, Math.max(b, Math.max(c, d)));
            }
        }
        long ans = maxPath[grid.length - 1][grid[0].length - 1][1];
        if (ans < 0) {
            return -1;
        }
        else {
            return (int)(ans % 1000000007);
        }
    }
}