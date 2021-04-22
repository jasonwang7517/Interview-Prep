public class addDigits {
    public int addDigits(int num) {
        int sum = Integer.MAX_VALUE;
        while (true) {
            char[] c = Integer.toString(num).toCharArray();
            int currSum = 0;
            for (char ch : c) {
                currSum += Character.getNumericValue(ch);
            }
            if (Integer.toString(currSum).length() == 1) {
                return currSum;
            }
            num = currSum;
        }
    }
}
