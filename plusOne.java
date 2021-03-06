public class plusOne {
    /*
    Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

    The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

    You may assume the integer does not contain any leading zero, except the number 0 itself.
     */
    public int[] plusOne(int[] digits) {
        if (digits[digits.length - 1] != 9) {
            digits[digits.length - 1] += 1;
            return digits;
        }
        else {
            int currVal = digits.length - 2;
        }
        return digits;
    }
}
