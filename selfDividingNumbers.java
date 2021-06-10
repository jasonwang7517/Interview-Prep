/*
    A self-dividing number is a number that is divisible by every digit it contains.
    - For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
    
    A self-dividing number is not allowed to contain the digit zero.

    Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
*/

import java.util.ArrayList;
import java.util.List;

class SelfDividingNumbers {
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