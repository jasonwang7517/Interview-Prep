/*
    Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

    For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of 
    candies among them. Notice that multiple kids can have the greatest number of candies.
*/

import java.util.ArrayList;
import java.util.List;

class KidsWithTheGreatestNumberofCandies {
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