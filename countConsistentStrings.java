class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int ans = 0;
        HashSet<Character> set = new HashSet<>();
        for (int i = 0; i < allowed.length(); i++) {
            set.add(allowed.charAt(i));
        }
        for (int i = 0; i < words.length; i++) {
            boolean toAdd = true;
            String s = words[i];
            for (int j = 0; j < s.length(); j++) {
                if (!set.contains(s.charAt(j))) {
                    toAdd = false;
                    break;
                }
            }
            if (toAdd) {
                ans++;
            }
        }
        return ans;
    }
}