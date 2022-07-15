/*
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
*/

public class AddDigits {
    public int addDigits(int num) {
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
