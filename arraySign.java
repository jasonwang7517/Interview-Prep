public class arraySign {
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
