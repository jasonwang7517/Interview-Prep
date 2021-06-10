/*
    There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to 
    perform some increment operations on the matrix.

    For each location indices[i], do both of the following:
    - Increment all the cells on row ri.
    - Increment all the cells on column ci.
    
    Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.
*/

public class CellsWithOddValuesInAMatrix {
    public static int oddCells(int n, int m, int[][] indices) {
        int ans = 0;
        int[][] arr = new int[n][m];
        for (int i = 0; i < indices.length; i++) {
            int ri = indices[i][0];
            int ci = indices[i][1];
            for (int j = 0; j < m; j++) {
                arr[ri][j] += 1;
            }
            for (int k = 0; k < n; k++) {
                arr[k][ci] += 1;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] % 2 == 1) {
                    ans++;
                }
            }
        }
        return ans;
    }
}
