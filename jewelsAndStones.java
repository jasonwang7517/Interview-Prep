import java.util.HashMap;
import java.util.HashSet;

public class jewelsAndStones {
    /*
    You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
    Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
    The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
    so "a" is considered a different type of stone from "A".
     */
    public int numJewelsInStones(String J, String S) {
        HashMap<Character, Integer> counts = new HashMap<Character, Integer>();
        int total = 0;
        for (char c : S.toCharArray()) {
            if (counts.containsKey(c)) {
                counts.put(c, counts.get(c) + 1);
            }
            else {
                counts.put(c, 1);
            }
        }
        for (char ch: J.toCharArray()) {
            if (counts.containsKey(ch)) {
                total += counts.get(ch);
            }
        }
        return total;
    }
}
