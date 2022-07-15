/*
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word 
if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.
*/

public class LengthOfLastWord {
    public static int lengthOfLastWord(String s) {
        int ans = 0;
        int finalAns = 0;
        if (s.length() == 0)
            return 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ' ')
                ans++;
            else if (s.charAt(i) == ' ' && ans != 0) {
                finalAns = ans;
                ans = 0;
            }
        }
        if (ans > 0)
            return ans;
        return finalAns;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLastWord("Hello World"));
        System.out.println(lengthOfLastWord("asdf "));
        System.out.println(lengthOfLastWord("b  "));
    }
}
