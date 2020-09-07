import java.lang.reflect.Array;
import java.util.Arrays;

public class oddCells {
    /*
    Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci].
    For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

    Return the number of cells with odd values in the matrix after applying the increment to all indices.
     */
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
        System.out.println(Arrays.deepToString(arr));
        return ans;
    }

    public static void main (String[] args) {
        int[][] test = new int[][]{{0,1}, {1, 1}};
        System.out.println(Arrays.deepToString(test));
        oddCells(2, 3, test);
    }
}
