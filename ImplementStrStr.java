/*
    Implement strStr().

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Clarification:

    What should we return when needle is an empty string? This is a great question to ask during an interview.

    For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
*/

public class ImplementStrStr {
    public static int strStr(String haystack, String needle) {
        if (haystack.equals("") && needle.equals(""))
            return 0;
        else if (needle.equals("")) {
            return 0;
        }
        else if (haystack.length() < needle.length())
            return -1;
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            for (int j = 0; j < needle.length(); j++) {
                if (j == needle.length() - 1 && haystack.charAt(i + j) == needle.charAt(j))
                    return i;
                else if (haystack.charAt(i + j) != needle.charAt(j)) {
                    break;
                }
            }
        }
        return -1;
    }
}
