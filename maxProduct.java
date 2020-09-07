public class maxProduct {
    /*
    Given the array of integers nums, you will choose two different indices i and j of that array.

    Return the maximum value of (nums[i]-1)*(nums[j]-1).
     */
    public int maxProduct(int[] nums) {
        int max1 = 0;
        int max2 = 0;
        for (int i : nums) {
            if (i > max1) {
                max2 = max1;
                max1 = i;
            }
            else if (i > max2) {
                max2 = i;
            }
        }
        return (max1 - 1) * (max2 - 1);
    }
}
