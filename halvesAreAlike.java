import java.util.Arrays;
import java.util.HashSet;

class halvesAreAlike {
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