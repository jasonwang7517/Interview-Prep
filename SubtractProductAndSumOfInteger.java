public class SubtractProductAndSumOfInteger {
/*
    Given an integer number n, return the difference between the product of its digits and the sum of its digits.
*/
    public static int subtractProductAndSum(int n) {
        int prod = 1;
        int sum = 0;
        String s = Integer.toString(n);
        int[] digits = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            digits[i] = Character.getNumericValue(s.charAt(i));
        }
        for (int i : digits) {
            System.out.println(i);
            prod *= i;
        };
        for (int i : digits) {
            sum += i;
        }
        return prod - sum;
    }
}
