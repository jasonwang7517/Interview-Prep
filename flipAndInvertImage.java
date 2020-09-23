public class flipAndInvertImage {
    /*
    Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

    To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

    To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
     */
    public int[][] flipAndInvertImage(int[][] A) {
        int[][] ans = new int[A.length][A[0].length];
        for (int i = 0; i < ans.length; i++) {
            for (int j = 0; j < ans[0].length; j++) {
                ans[i][j] = A[i][A.length - 1 - j];
            }
            for (int k = 0; k < ans.length; k++) {
                if (ans[i][k] == 0) {
                    ans[i][k] = 1;
                }
                else {
                    ans[i][k] = 0;
                }
            }
        }
        return ans;
    }

}
