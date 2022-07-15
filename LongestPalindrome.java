/*
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
*/

 import java.util.HashMap;

class LongestPalindrome {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> counts = new HashMap<>(); 
        for (int i = 0; i < s.length(); i++) {
            if (counts.containsKey(s.charAt(i))) {
                counts.put(s.charAt(i), counts.get(s.charAt(i)) + 1);
            }
            else {
                counts.put(s.charAt(i), 1);
            }
        }
        int ans = 0;
        boolean odd = false;
        for (Character c : counts.keySet()) {
            if (counts.get(c) % 2 == 0) {
                ans += counts.get(c);
            }
            else if (counts.get(c) % 2 == 1) {
                ans += counts.get(c) - 1;
                odd = true;
            }
        }
        if (odd) {
            return ans + 1;
        }
        return ans;
    }
}