public class isPalindromeEx {
    /*
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.
     */
    public static boolean isPalindrome(String s) {
        if (s.equals("")) {
            return true;
        }
        s = s.toLowerCase();
        int front = 0;
        int back = s.length() - 1;
        while (front <= back) {
            char frontChar = s.charAt(front);
            char backChar = s.charAt(back);
            if (Character.isLetterOrDigit(frontChar) && Character.isLetterOrDigit(backChar)) {
                if (frontChar != backChar) {
                    return false;
                }
                front++;
                back--;
            }
            else if (!Character.isLetterOrDigit(frontChar)) {
                front++;
            }
            else if (!Character.isLetterOrDigit(backChar)) {
                back--;
            }
        }
        return true;
    }

    public static void main (String[] args) {
        System.out.println(isPalindrome("Level"));
    }
}
