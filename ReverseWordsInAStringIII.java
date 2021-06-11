/*
    Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
*/

public class ReverseWordsInAStringIII {
    public String reverseWords(String s) {
        String ans = "";
        String[] components = s.split(" ");
        for (String str : components) {
            for (int i = str.length() - 1; i >= 0; i--) {
                ans += str.charAt(i);
            }
            ans += " ";
        }
        return ans.substring(0, ans.length() - 1);
    }
}