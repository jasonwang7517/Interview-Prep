/*
Given a string s. You should re-order the string using the following algorithm:
    1. Pick the smallest character from s and append it to the result.
    2. Pick the smallest character from s which is greater than the last appended character to the result and append it.
    3. Repeat step 2 until you cannot pick more characters.
    4. Pick the largest character from s and append it to the result.
    5. Pick the largest character from s which is smaller than the last appended character to the result and append it.
    6. Repeat step 5 until you cannot pick more characters.
    7. Repeat the steps from 1 to 6 until you pick all characters from s.
    
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
*/

public class IncreasingDecreasingString {
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
}
