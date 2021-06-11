/*
    Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
*/

import java.util.HashMap;
import java.util.HashSet;

public class UniqueNumberOfOccurences {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        HashSet<Integer> freq = new HashSet<>();
        for (int i : arr) {
            if (map.containsKey(i)) {
                map.put(i, map.get(i) + 1);
            }
            else {
                map.put(i, 1);
            }
        }
        for (int i : map.keySet()) {
            if (freq.contains(map.get(i))) {
                return false;
            }
            else {
                freq.add(map.get(i));
            }
        }
        return true;
    }
}