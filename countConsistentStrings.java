/*
    You are given a string allowed consisting of distinct characters and an array of strings words. A string is
    consistent if all characters in the string appear in the string allowed.

    Return the number of consistent strings in the array words.

    Constraints:
    - 1 <= words.length <= 104
    - 1 <= allowed.length <= 26
    - 1 <= words[i].length <= 10
    - The characters in allowed are distinct.
    - words[i] and allowed contain only lowercase English letters.
 */

import java.util.HashSet;

class countConsistentStrings {
    public int countConsistentStrings(String allowed, String[] words) {
        int ans = 0;
        HashSet<Character> set = new HashSet<>();
        for (int i = 0; i < allowed.length(); i++) {
            set.add(allowed.charAt(i));
        }
        for (int i = 0; i < words.length; i++) {
            boolean toAdd = true;
            String s = words[i];
            for (int j = 0; j < s.length(); j++) {
                if (!set.contains(s.charAt(j))) {
                    toAdd = false;
                    break;
                }
            }
            if (toAdd) {
                ans++;
            }
        }
        return ans;
    }
}