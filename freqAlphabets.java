import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class freqAlphabets {
    /*
    Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

    Return the string formed after mapping.

    It's guaranteed that a unique mapping will always exist.
     */
    public static String freqAlphabets(String s) {
        String str = "";
        Stack<Character> stack = new Stack<>();
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '#') {
                String temp = s.substring(i - 2, i + 1);
                int charIndex = Integer.parseInt(temp.substring(0, 2));
                System.out.println((char)('a' + charIndex - 1));
                stack.push((char)('a' + charIndex - 1));
                i -= 2;
            }
            else {
                System.out.println((char)('a' + Character.getNumericValue(s.charAt(i)) - 1));
                stack.push((char)('a' + Character.getNumericValue(s.charAt(i)) - 1));
            }
        }
        while (!stack.isEmpty()) {
            str += stack.pop();
        }
        return str;
    }

    public static void main(String[] args) {
        String test = "10#11#12";
        System.out.println(freqAlphabets(test));
    }
}
