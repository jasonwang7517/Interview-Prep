import java.util.HashSet;

public class checkIfPangram {
    public boolean checkIfPangram(String sentence) {
        String letters = "abcdefghijklmnopqrstuvwxyz";
        HashSet<Character> seen = new HashSet<>();
        for (char c : sentence.toCharArray()) {
            if (!seen.contains(c)) {
                seen.add(c);
            }
        }
        for (char c : letters.toCharArray()) {
            if (!seen.contains(c)) {
                return false;
            }
        }
        return true;
    }
}
