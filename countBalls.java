public class countBalls {
    public int countBalls(int lowLimit, int highLimit) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int i = lowLimit; i <= highLimit; i++) {
            int sum = 0;
            String s = Integer.toString(i);
            for (int j = 0; j < s.length(); j++) {
                sum += Character.getNumericValue(s.charAt(j));
            }
            if (hm.containsKey(sum)) {
                hm.put(sum, hm.get(sum) + 1);
            }
            else {
                hm.put(sum, 1);
            }
        }
        int currMax = 0;
        for (int i : hm.keySet()) {
            if (hm.get(i) > currMax) {
                currMax = hm.get(i);
            }
        }
        return currMax;
    }
}
