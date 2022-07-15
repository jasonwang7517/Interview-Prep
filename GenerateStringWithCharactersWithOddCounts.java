/*
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.
*/
public class GenerateStringWithCharactersWithOddCounts {
    public String generateTheString(int n) {
        String s = "";
        if (n % 2 == 1) {
            for (int i = 0; i < n; i++) {
                s += "a";
            }
        }
        else {
            for (int i = 0; i < n - 1; i++) {
                s += "a";
            }
            s += "b";
        }
        return s;
    }
}
