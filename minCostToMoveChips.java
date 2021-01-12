class Solution {
    public int minCostToMoveChips(int[] position) {
        int count0 = 0;
        int count1 = 0;
        if (position.length == 1) {
            return 0;
        }
        for (int i = 0; i < position.length; i++) {
            if (position[i] % 2 == 0) {
                count0++;
            }
            else if (position[i] % 2 == 1) {
                count1++;
                
            }
        }
        return Math.min(count0, count1);
    }
}