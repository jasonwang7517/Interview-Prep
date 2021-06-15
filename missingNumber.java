/*
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
*/

import java.util.HashSet;

public class MissingNumber {
    public int missingNumber(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i <= nums.length; i++) {
            set.add(i);
        }
        for (int i : nums) {
            set.remove(i);
        }
        int ans = 0;
        for (int i : set) {
            ans = i;
        }
        return ans;
    }
}