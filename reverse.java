import java.util.Arrays;

public class reverse {
    public static int reverse(int x) {
        char[] chars = Integer.toString(x).toCharArray();
        String s = "";
        if (chars[0] == '-') {
            for (int i = chars.length - 1; i > 0; i--) {
                s += chars[i];
            }
            s = "-" + s;
        }
        else {
            for (int i = chars.length - 1; i >= 0; i--) {
                s += chars[i];
            }
        }
        if (s.length() == 10 && s.charAt(0) != '-') {
            String max = Integer.toString(Integer.MAX_VALUE);
            char[] sChars = s.toCharArray();
            char[] maxChars = max.toCharArray();
            for (int i = 0; i < s.length(); i++) {
                if (Character.getNumericValue(sChars[i]) < Character.getNumericValue(maxChars[i])) {
                    break;
                }
                else if (Character.getNumericValue(sChars[i]) > Character.getNumericValue(maxChars[i])) {
                    s = "0";
                    break;
                }
            }
        }
        else if (s.length() == 11 && s.charAt(0) == '-') {
            String min = Integer.toString(Integer.MIN_VALUE);
            char[] sChars = s.toCharArray();
            char[] maxChars = min.toCharArray();
            for (int i = 1; i < s.length(); i++) {
                if (Character.getNumericValue(sChars[i]) < Character.getNumericValue(maxChars[i])) {
                    break;
                }
                else if (Character.getNumericValue(sChars[i]) > Character.getNumericValue(maxChars[i])) {
                    s = "0";
                    break;
                }
            }
        }
        return Integer.valueOf(s);
    }

    public static void main (String[] args) {
        System.out.println(reverse(-2147483648));
    }
}
