/*
    A pangram is a sentence where every letter of the English alphabet appears at least once.

    Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
*/

import java.util.HashSet;

public class CheckIfSentenceIsPangram {
    public boolean checkIfPangram(String sentence) {
        HashSet<Character> seen = new HashSet<>();
        for (char c : sentence.toCharArray()) {
            if (!seen.contains(c)) {
                seen.add(c);
                if (seen.size() == 26) {
                    return true;
                }
            }
        }
        return false;
    }
}
