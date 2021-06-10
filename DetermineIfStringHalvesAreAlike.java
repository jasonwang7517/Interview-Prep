/*
    You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

    Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

    Return true if a and b are alike. Otherwise, return false.
*/

import java.util.Arrays;
import java.util.HashSet;

class DetermineIfStringHalvesAreAlike {
    public boolean halvesAreAlike(String s) {
        int numVowels = 0;
        HashSet<Character> vowel = new HashSet<>();
        vowel.addAll(Arrays.asList(new Character[] {'a', 'e', 'i', 'o', 'u'}));
        for (int i = 0; i < s.length() / 2; i++) {
            if (vowel.contains(Character.toLowerCase(s.charAt(i)))) {
                numVowels++;
            }
        }
        for (int i = s.length() / 2; i < s.length(); i++) {
            if (vowel.contains(Character.toLowerCase(s.charAt(i)))) {
                numVowels--;
            }
        }
        return numVowels == 0;
    }
}