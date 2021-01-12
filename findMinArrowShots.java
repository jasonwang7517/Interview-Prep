class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) {
            return 0;
        }
        else if (points.length == 1) {
            return 1;
        }
        Arrays.sort(points, new java.util.Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });
        int minEnd = points[0][1];
        int arrows = 1;
        for (int[] i : points) {
            if (i[0] > minEnd) {
                arrows++;
                minEnd = i[1];
            }
            else if (i[1] < minEnd) {
                minEnd = i[1];
            }
        }
        return arrows;
    }
}