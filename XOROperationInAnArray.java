/*
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
*/

public class XOROperationInAnArray {
    public int xorOperation(int n, int start) {
        int[] nums = new int[n];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = start + (2 * i);
        }
        int ans = nums[0];
        for (int i = 1; i < nums.length; i++){
            ans ^= nums[i];
        }
        return ans;
    }
}
