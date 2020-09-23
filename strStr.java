public class strStr {
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

    public static void main (String[] args) {
        System.out.println(strStr("hello", "ll"));
        System.out.println(strStr("aaaaa", "bba"));
        System.out.println(strStr("a", "a"));
        System.out.println(strStr("mississippi", "issip"));
    }
}
