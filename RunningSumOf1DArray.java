/*
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
*/

public class RunningSumOf1DArray{
    public int[] runningSum(int[] nums) {
        int[] runningSum = new int[nums.length];
        runningSum[0] = nums[0];
        for (int i = 1; i < runningSum.length; i++){
            runningSum[i] = runningSum[i-1] + nums[i];
        }
        return runningSum;
    }
}
