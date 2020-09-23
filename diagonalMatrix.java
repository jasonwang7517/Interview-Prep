public class diagonalMatrix {
    /*
    Given a square matrix mat, return the sum of the matrix diagonals.

    Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
     */
    public int diagonalSum(int[][] mat) {
        int ans = 0;
        for (int i = 0; i < mat.length; i++) {
            ans+= mat[i][i];
        }
        int rowIndex = mat.length - 1;
        int colIndex = 0;
        for (int i = 0; i < mat.length; i++) {
            ans += mat[rowIndex][colIndex];
            rowIndex--;
            colIndex++;
        }
        if (mat.length % 2 == 1) {
            ans -= mat[(mat.length - 1) / 2][(mat.length - 1) / 2];
        }
        return ans;
    }
}
