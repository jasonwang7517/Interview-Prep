/**
We define the usage of capitals in a word to be right when one of the following cases holds:
    - All letters in this word are capitals, like "USA".
    - All letters in this word are not capitals, like "leetcode".
    - Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.
 */

class DetectCapital {
    public boolean detectCapitalUse(String word) {
        int numCapitals = 0;
        for (char c : word.toCharArray()) {
            int order = (int) c;
            if (order <= (int) 'Z') {
                numCapitals++;
            }
        }
        return numCapitals == 0 || numCapitals == word.length() || (numCapitals == 1 && (int) word.charAt(0) <= (int) 'Z');
    }
}