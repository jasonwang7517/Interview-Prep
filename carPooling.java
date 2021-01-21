class carPooling {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] timeline = new int[1001];
        for (int i = 0; i < trips.length; i++) {
            timeline[trips[i][1]] += trips[i][0];
            timeline[trips[i][2]] -= trips[i][0];
        }
        int currCap = 0;
        for (int i : timeline) {
            currCap += i;
            if (currCap > capacity) {
                return false;
            }
        }
        return true;
    }
}