/*
There is a function signFunc(x) that returns:
    - 1 if x is positive.
    - -1 if x is negative.
    - 0 if x is equal to 0.
    - You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
*/

public class SignOfTheProductOfAnArray {
    public int arraySign(int[] nums) {
        int negativeCounts = 0;
        for (int i : nums) {
            if (i == 0) {
                return 0;
            }
            else if (i < 0) {
                    negativeCounts++;
                }
        }
        if (negativeCounts % 2 == 0) {
            return 1;
        }
        else {
            return -1;
        }
    }
}
