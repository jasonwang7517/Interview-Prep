/*
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-...").
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.
*/

import java.util.HashSet;
import java.util.Set;

public class UniqueMorseCodeWords {
    public static int uniqueMorseRepresentations(String[] words) {
        String[] morse = new String[]{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
                "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        Set<String> ans = new HashSet<String>();
        for (String s : words) {
            String str = "";
            char[] arr = s.toCharArray();
            for (char c : arr) {
                str += morse[c - 'a'];
            }
            ans.add(str);
        }
        return ans.size();
    }
}
