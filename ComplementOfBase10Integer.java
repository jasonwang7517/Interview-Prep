/*
Every non-negative integer n has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except 
for n = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary 
is "010" in binary.

For a given number n in base-10, return the complement of it's binary representation as a base-10 integer.
*/

public class ComplementOfBase10Integer {
    public int bitwiseComplement(int N) {
        String bin = Integer.toBinaryString(N);
        String ans = "";
        for (int i = 0; i < bin.length(); i++) {
            if (bin.charAt(i) == '0') {
                ans += '1';
            }
            else{
                ans += '0';
            }
        }
        return Integer.parseInt(ans, 2);
    }
}
