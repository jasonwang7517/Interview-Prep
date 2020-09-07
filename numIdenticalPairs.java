import java.util.HashMap;

public class numIdenticalPairs {
    /*
    Given an array of integers nums.
    A pair (i,j) is called good if nums[i] == nums[j] and i < j.
    Return the number of good pairs.
    */

    /*Brute Force
    * Time: O(N^2)
    * Space: O(1)
    */
    public static int numIdenticalPairs(int[] nums) {
        int numGoodPairs = 0;
        for (int i  = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    System.out.println("i = " + i);
                    System.out.println("j = " + j);
                    numGoodPairs++;
                }
            }
        }
        return numGoodPairs;
    }
}
