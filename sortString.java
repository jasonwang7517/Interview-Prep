import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.TreeMap;

public class sortString {
    public static String sortString(String s) {
        String str = "";
        int[] ans = new int[26];
        char[] chars = s.toCharArray();
        for (char c: chars) {
            ans[c - 'a'] += 1;
        }
        while (str.length() != s.length()) {
            for (int i = 0; i < 26; i++) {
                if (ans[i] > 0) {
                    str += (char) ('a' + i);
                    ans[i] -= 1;
                }
            }
            for (int i = 25; i >= 0; i--) {
                if (ans[i] > 0) {
                    str += (char) ('a' + i);
                    ans[i] -= 1;
                }
            }
        }
        return str;
    }

    public static void main (String[] args) {
        System.out.println(sortString("leetcode"));
    }
}
