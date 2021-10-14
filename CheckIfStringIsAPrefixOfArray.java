/**
Given a string s and an array of strings words, determine whether s is a prefix string of words.

A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.
*/

class CheckIfStringIsAPrefixOfArray {
    public boolean isPrefixString(String s, String[] words) {
        StringBuilder ans = new StringBuilder ("");
        for (String st : words) {
            ans.append(st);
            if (s.equals (ans.toString()))
                return true;
            if (s.indexOf (ans.toString()) == -1)
                return false;
        }
        return false;
    }
}