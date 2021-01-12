class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        ArrayList<Integer> ans = new ArrayList<>();
        for (int i = left; i <= right; i++) {
            String s = Integer.toString(i);
            char[] c = s.toCharArray();
            boolean canAdd = true;
            for (char ch : c) {
                int curr = Character.getNumericValue(ch);
                if (curr == 0 || i % curr != 0) {
                    canAdd = false;
                    break;
                }
            }
            if (canAdd)
                ans.add(i);
        }
        return ans;
    }
}