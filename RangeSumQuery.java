/*
Given an integer array nums, handle multiple queries of the following type:
    1. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:
    - NumArray(int[] nums) Initializes the object with the integer array nums.
    - int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
*/

class NumArray {
    
    int[] runningSum;

    public NumArray(int[] nums) {
        runningSum = new int[nums.length];
        runningSum[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            runningSum[i] = runningSum[i - 1] + nums[i];
        }
    }
    
    public int sumRange(int left, int right) {
        if (left == 0) {
            return runningSum[right];
        }
        return runningSum[right] - runningSum[left - 1];
    }
}