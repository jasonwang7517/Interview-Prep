class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxWealth = 0;
        for (int i = 0; i < accounts.length; i++) {
            int currVal = 0;
            for (int j = 0; j < accounts[0].length; j++) {
                currVal += accounts[i][j];
            }
            if (currVal > maxWealth)
                maxWealth = currVal;
        }
        return maxWealth;
    }
}