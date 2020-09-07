public class max69Number {
    /*
    Given a positive integer num consisting only of digits 6 and 9.

    Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
     */
    public static int maximum69Number (int num) {
        char[] arr = Integer.toString(num).toCharArray();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == '6') {
                arr[i] = '9';
                break;
            }
        }
        return Integer.parseInt(new String(arr));
    }

    public static void main (String[] args) {
        System.out.println(maximum69Number(9669));
    }
}
