import java.util.ArrayList;

public class decompressRLEList {
    /*
    We are given a list nums of integers representing a list compressed with run-length encoding.

    Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair,
    there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right
    to generate the decompressed list.

    Return the decompressed list.
     */
    public static int[] decompressRLElist(int[] nums) {
        ArrayList<Integer> count = new ArrayList<>();
        for (int i = 0; i < nums.length - 1; i += 2) {
            int freq = nums[i];
            int currNum = nums[i + 1];
            while (freq > 0) {
                count.add(currNum);
                freq--;
            }
        }
        int[] ans = new int[count.size()];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = count.get(i);
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(decompressRLElist(new int[]{1, 2, 3, 4}));
    }
}
