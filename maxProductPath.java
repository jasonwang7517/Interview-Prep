class maxProductPath {
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