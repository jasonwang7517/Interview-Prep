/*
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
    then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
*/

public class ReverseInteger {
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
}
