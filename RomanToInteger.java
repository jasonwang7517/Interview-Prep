/*
Given a roman numeral, convert it to an integer.
*/

import java.util.HashMap;

public class RomanToInteger {
    public static int romanToInt(String s) {
        int ans = 0;
        HashMap<Character, Integer> vals = new HashMap<>();
        vals.put('I', 1);
        vals.put('V', 5);
        vals.put('X', 10);
        vals.put('L', 50);
        vals.put('C', 100);
        vals.put('D', 500);
        vals.put('M', 1000);
        for (int i = 0; i < s.length() - 1; i++) {
            char c = s.charAt(i);
            char cAfter = s.charAt(i + 1);
            if (vals.get(c) < vals.get(cAfter)) {
                ans += (vals.get(cAfter) - vals.get(c));
                i++;
                if (i == s.length() - 1) {
                    return ans;
                }
            }
            else {
                ans += vals.get(c);
            }
        }
        ans += vals.get(s.charAt(s.length() - 1));
        return ans;
    }

    public static void main (String[] args) {
        System.out.println(romanToInt("III"));
        System.out.println(romanToInt("IV"));
        System.out.println(romanToInt("IX"));
        System.out.println(romanToInt("LVIII"));
        System.out.println(romanToInt("MCMXCIV"));
    }
}
