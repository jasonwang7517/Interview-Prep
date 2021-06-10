/*
    Given an array nums of integers, return how many of them contain an even number of digits.
*/

public class FindNumbersWithEvenNumberOfDigits {
    public int findNumbers(int[] nums) {
        int ans = 0;
        for (int i: nums) {
            String s = Integer.toString(i);
            if (s.length() % 2 == 0) {
                ans++;
            }
        }
        return ans;
    }
}
