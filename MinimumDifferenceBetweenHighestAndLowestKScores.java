/**
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.
 */

 import java.util.*;

class MinimumDifferenceBetweenHighestAndLowestKScores {
    public int minimumDifference(int[] nums, int k) {
        if (nums.length <= 1) {
            return 0;
        }
        Arrays.sort(nums);
        int minimum = Integer.MAX_VALUE;
        int start = 0;
        while (start < nums.length - k + 1) {
            if (nums[start + k - 1] - nums[start] < minimum) {
                minimum = nums[start + k - 1] - nums[start];
            }
            start++;
        }
        return minimum;
    }
}