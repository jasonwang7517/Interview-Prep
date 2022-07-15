/*
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
*/

public class FindWordsThatCanBeFormedByCharacters {
    public int countCharacters(String[] words, String chars) {
        int ans = 0;
        int[] charCounts = new int[26];
        for (char c : chars.toCharArray()) {
            int index = c - 'a';
            charCounts[index] += 1;
        }
        for (String s : words) {
            int[] charCounts2 = new int[26];
            for (char c : s.toCharArray()) {
                int index = c - 'a';
                charCounts2[index] += 1;
            }
            boolean good = true;
            for (int i = 0; i < 26; i++) {
                if (charCounts2[i] > charCounts[i]) {
                    good = false;
                }
            }
            if (good) {
                ans += s.length();
            }
        }
        return ans;
    }
}
