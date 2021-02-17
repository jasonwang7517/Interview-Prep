public class check {
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
