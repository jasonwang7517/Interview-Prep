/*
    Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
*/

public class ValidPalindrome {
    public static boolean isPalindrome(String s) {
        if (s.equals("")) {
            return true;
        }
        int front = 0;
        int back = s.length() - 1;
        s = s.toLowerCase();
        while (front <= back) {
            char frontChar = s.charAt(front);
            char backChar = s.charAt(back);
            if (Character.isLetterOrDigit(frontChar) && Character.isLetterOrDigit(backChar)) {
                if (frontChar != backChar) {
                    return false;
                }
                else {
                    front++;
                    back--;
                }
            }
            else if (!Character.isLetterOrDigit(s.charAt(front))) {
                front++;
            }
            else if (!Character.isLetterOrDigit(s.charAt(back))) {
                back--;
            }
        }
        return true;
    }

    public static void main (String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama"));
    }
}
