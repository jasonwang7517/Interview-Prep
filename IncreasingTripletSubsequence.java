/*
    Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices 
    exists, return false.
*/

public class IncreasingTripletSubsequence {
    public boolean increasingTriplet(int[] nums) {
        int largest = Integer.MAX_VALUE;
        int smallest = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= smallest) {
                smallest = nums[i];
            }
            else if (nums[i] <= largest) {
                largest = nums[i];
            }
            else if (nums[i] > largest && smallest < largest) {
                return true;
            }
        }
        return false;
    }
}