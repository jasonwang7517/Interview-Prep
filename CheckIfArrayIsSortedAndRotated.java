/*
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). 

Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
*/

public class CheckIfArrayIsSortedAndRotated {
    public boolean check(int[] nums) {
        int breaks = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > nums[(i + 1) % nums.length]) {
                breaks++;
            }
            if (breaks > 1) {
                return false;
            }
        }

        return true;
    }
}
