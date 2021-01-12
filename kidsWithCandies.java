class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        for (int candy : candies) {
            if (candy > max) {
                max = candy;
            }
        }
        List<Boolean> greatestCandies = new ArrayList<>();
        for (int candy : candies) {
            if (max - candy <= extraCandies) {
                greatestCandies.add(true);
            }
            else {
                greatestCandies.add(false);
            }
        }
        return greatestCandies;
    }
}