/*
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and 
you may return the result in any order.
*/

import java.util.*;

class IntersectionOfTwoArraysII {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> counts1 = new HashMap<>();
        for (int i : nums1) {
            if (counts1.containsKey(i)) {
                counts1.put(i, counts1.get(i) + 1);
            }
            else {
                counts1.put(i, 1);
            }
        }
        HashMap<Integer, Integer> counts2 = new HashMap<>();
        for (int i : nums2) {
            if (counts2.containsKey(i)) {
                counts2.put(i, counts2.get(i) + 1);
            }
            else {
                counts2.put(i, 1);
            }
        }
        ArrayList<Integer> ans = new ArrayList<>();
        for (int i : counts1.keySet()) {
            if (counts2.containsKey(i)) {
                int instances = Math.min(counts1.get(i), counts2.get(i));
                for (int j = 0; j < instances; j++) {
                    ans.add(i);
                }
            }
        }
        int[] finalAns = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            finalAns[i] = ans.get(i);
        }
        return finalAns;
    }
}