public class longestCommonPrefix {
    public static String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        if (strs.length == 1) {
            return strs[0];
        }
        String pref = strs[0];
        int index = 1;
        while (pref != "" && index < strs.length) {
            String curr = strs[index];
            if (curr.equals("")) {
                return "";
            }
            for (int i = 0; i < curr.length(); i++) {
                if (i >= pref.length()) {
                    break;
                }
                else if (pref.charAt(i) != curr.charAt(i)) {
                    pref = pref.substring(0, i);
                    break;
                }
                else if (i == curr.length() - 1) {
                    pref = pref.substring(0, i + 1);
                }
            }
            index++;
        }
        return pref;
    }

    public static void main(String[] args) {
        String[] test = new String[]{"aa", "a"};
        System.out.println(longestCommonPrefix(test));
    }
}
