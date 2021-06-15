/*
    Given an array of integers nums and and integer target, return the indices of the two numbers such that
    they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
*/

import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        HashMap<Integer, Integer> diffs = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
           int comp = target - nums[i];
           if (diffs.containsKey(comp)) {
               ans[0] = i;
               ans[1] = diffs.get(comp);
               break;
           }
           else {
               diffs.put(nums[i], i);
           }
        }
        return ans;
    }
}
