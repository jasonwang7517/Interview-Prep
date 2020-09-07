public class balancedStringSplit {
    /*
    Balanced strings are those who have equal quantity of 'L' and 'R' characters.

    Given a balanced string s split it in the maximum amount of balanced strings.

    Return the maximum amount of splitted balanced strings.
     */
    public int balancedStringSplit(String s) {
        int ans = 0;
        int numL = 0;
        int numR = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'L')
                numL++;
            else
                numR++;
            if (numL == numR) {
                ans++;
                numL = 0;
                numR = 0;
            }
        }
        return ans;
    }
}
