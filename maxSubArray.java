public class maxSubArray {
    /*
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
     */
    public static int maxSubArray(int[] nums) {
        int max = nums[0];
        int maxEndingHere = nums[0];
        for (int i = 1; i < nums.length; i++) {
            maxEndingHere = Math.max(maxEndingHere + nums[i], nums[i]);
            max = Math.max(maxEndingHere, max);
        }
        return max;
    }

    public static void main(String[] args) {
        int[] test = new int[]{1, 2};
        int[] test2 = new int[]{0};
        int[] test3 = new int[]{-2,1,-3,4,-1,2,1,-5,4};
        int[] test4 = new int[]{-2, 1};
        System.out.println(maxSubArray(test3));
        System.out.println(maxSubArray(test2));
        System.out.println(maxSubArray(test));
        System.out.println(maxSubArray(test4));
    }
}
