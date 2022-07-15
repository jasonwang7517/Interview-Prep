/*
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
*/

public class PalindromeNumber {
    public boolean isPalindrome(int x) {
        char[] c = Integer.toString(x).toCharArray();
        for (int i = 0; i < c.length; i++) {
            if (c[i] != c[c.length - 1- i]) {
                return false;
            }
        }
        return true;
    }
}
