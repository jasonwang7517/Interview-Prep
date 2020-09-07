public class minTimeToVisitAllPoints {
    /*
    On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

    You can move according to the next rules:

    In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
    You have to visit the points in the same order as they appear in the array.
     */
    public static int minTimeToVisitAllPoints(int[][] points) {
        int ans = 0;
        for (int i = 0; i < points.length - 1; i++)
        {
            int currX = points[i][0];
            int currY = points[i][1];
            int goalX = points[i + 1][0];
            int goalY = points[i + 1][1];
            while ((currX != goalX) || (currY != goalY)) {
                if (currX != goalX && currY == goalY) {
                    ans += Math.abs(goalX - currX);
                    currX += goalX - currX;
                }
                else if (currY != goalY && currX == goalX) {
                    ans += Math.abs(goalY - currY);
                    currY += goalY - currY;
                }
                else if (currX < goalX && currY < goalY) {
                    int xDiff = goalX - currX;
                    int yDiff = goalY - currY;
                    if (xDiff <= yDiff) {
                        ans += Math.abs(xDiff);
                        currX += xDiff;
                        currY += xDiff;
                    }
                    else if (yDiff < xDiff) {
                        ans += Math.abs(yDiff);
                        currX += yDiff;
                        currY += yDiff;
                    }
                }
                else if (currX > goalX && currY > goalY) {
                    int xDiff = currX - goalX;
                    int yDiff = currY - goalY;
                    if (xDiff <= yDiff) {
                        ans += Math.abs(xDiff);
                        currX -= xDiff;
                        currY -= xDiff;
                    }
                    else if (yDiff < xDiff) {
                        ans += Math.abs(yDiff);
                        currX -= yDiff;
                        currY -= yDiff;
                    }
                }
                else if (currX < goalX && currY > goalY) {
                    int xDiff = goalX - currX;
                    int yDiff = currY - goalY;
                    if (xDiff <= yDiff) {
                        ans += Math.abs(xDiff);
                        currX += xDiff;
                        currY -= xDiff;
                    }
                    else if (yDiff < xDiff) {
                        ans += Math.abs(yDiff);
                        currX += yDiff;
                        currY -= yDiff;
                    }
                }
                else if (currX > goalX && currY < goalY) {
                    int xDiff = currX - goalX;
                    int yDiff = goalY - currY;
                    if (xDiff <= yDiff) {
                        ans += Math.abs(xDiff);
                        currX -= xDiff;
                        currY += xDiff;
                    }
                    else if (yDiff < xDiff) {
                        ans += Math.abs(yDiff);
                        currX -= yDiff;
                        currY += yDiff;
                    }
                }
            }
        }
        return ans;
    }
    public static void main (String[] args) {
        int[][] test = {{1, 1}, {3, 4}};
        minTimeToVisitAllPoints(test);
    }
}
