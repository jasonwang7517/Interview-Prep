public class searchInsert {
    /*
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.
     */
    public int searchInsert(int[] nums, int target) {
        int min = 0;
        int max = nums.length;
        while (min < max) {
            int middle = (min + max) / 2;
            if (nums[middle] > target)
                min = middle + 1;
            else
                max = middle;
        }
        return min;
    }
}
