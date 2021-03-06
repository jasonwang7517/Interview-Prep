public class nearestValidPoint {
    public int nearestValidPoint(int x, int y, int[][] points) {
        int ans = -1;
        int currDist = Integer.MAX_VALUE;
        for (int i = 0; i < points.length; i++) {
            int tempDistance = Integer.MAX_VALUE;
            if (points[i][0] == x && points[i][1] == y) {
                return i;
            }
            if (points[i][0] == x) {
                tempDistance = Math.abs(points[i][1] - y);
            }
            else if (points[i][1] == y) {
                tempDistance = Math.abs(points[i][0] - x);
            }
            if (tempDistance < currDist) {
                ans = i;
                currDist = tempDistance;
            }
        }
        return ans;
    }
}
