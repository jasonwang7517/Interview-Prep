/*
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum
*/

public class MaximumSubArray {
    public static int maxSubArray(int[] nums) {
        int max = nums[0];
        int maxEndingHere = nums[0];
        for (int i = 1; i < nums.length; i++) {
            maxEndingHere = Math.max(maxEndingHere + nums[i], nums[i]);
            max = Math.max(maxEndingHere, max);
        }
        return max;
    }
}
