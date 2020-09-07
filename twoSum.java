import java.util.HashMap;

public class twoSum {
    /*
    Given an array of integers nums and and integer target, return the indices of the two numbers such that
    they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
     */

    //Brute Force
    // Space: O(1)
    // Time: O(N^2)
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    ans[0] = i;
                    ans[1] = j;
                }
            }
        }
        return ans;
    }

    //Brute Force
    // Space: O(N)
    // Time: O(N)
    public int[] twoSumV2(int[] nums, int target) {
        int[] ans = new int[2];
        HashMap<Integer, Integer> diffs = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            diffs.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if (diffs.containsKey(comp) && diffs.get(comp) != i) {
                ans[0] = i;
                ans[1] = diffs.get(comp);
            }
        }
        return ans;
    }

    //Brute Force
    // Space: O(N)
    // Time: O(N)
    public int[] twoSumV3(int[] nums, int target) {
        int[] ans = new int[2];
        HashMap<Integer, Integer> diffs = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if (diffs.containsKey(comp)) {
                ans[0] = i;
                ans[1] = diffs.get(comp);
            }
            else {
                diffs.put(nums[i], i);
            }
        }
        return ans;
    }
}
