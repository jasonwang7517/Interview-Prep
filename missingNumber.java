import java.util.HashSet;

class missingNumber {
    public int missingNumber(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i <= nums.length; i++) {
            set.add(i);
        }
        for (int i : nums) {
            set.remove(i);
        }
        int ans = 0;
        for (int i : set) {
            ans = i;
        }
        return ans;
    }
}