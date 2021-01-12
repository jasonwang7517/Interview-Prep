class Solution {
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