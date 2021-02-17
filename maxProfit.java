class maxProfit {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int minPrice = Integer.MAX_VALUE;
        for (int i : prices) {
            if (i < minPrice) {
                minPrice = i;
            }
            else if (i - minPrice > profit) {
                profit = i - minPrice;
            }
        }
        return profit;
    }
}