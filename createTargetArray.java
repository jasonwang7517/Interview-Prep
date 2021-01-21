public class createTargetArray {
    /*
    Given two arrays of integers nums and index. Your task is to create target array under the following rules:
        - Initially target array is empty.
        - From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
        - Repeat the previous step until there are no elements to read in nums and index.

    Return the target array.

    It is guaranteed that the insertion operations will be valid.

    Constraints:
        - 1 <= nums.length, index.length <= 100
        - nums.length == index.length
        - 0 <= nums[i] <= 100
        - 0 <= index[i] <= i
     */
    public int[] createTargetArray(int[] nums, int[] index) {
        int[] ans = new int[nums.length];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = -1;
        }
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int indexVal = index[i];
            if (ans[indexVal] == -1) {
                ans[indexVal] = num;
            }
            else {
                for (int j = nums.length - 1; j > indexVal; j--) {
                    ans[j] = ans[j-1];
                }
                ans[indexVal] = num;
            }
        }
        return ans;
    }
}
