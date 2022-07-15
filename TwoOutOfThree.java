/*
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays.
 
You may return the values in any order.
*/

import java.util.*;

class TwoOutOfThree {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        HashSet<Integer> set1 = new HashSet<>();
        for (int i : nums1) {
            set1.add(i);
        }
        HashSet<Integer> set2 = new HashSet<>();
        for (int i : nums2) {
            set2.add(i);
        }
        HashSet<Integer> set3 = new HashSet<>();
        for (int i : nums3) {
            set3.add(i);
        }
        HashSet<Integer> ansSet = new HashSet<>();
        for (int i : set1) {
            if (set2.contains(i) || set3.contains(i)) {
                ansSet.add(i);
            }
        }
        for (int i : set2) {
            if (set3.contains(i)) {
                ansSet.add(i);
            }
        }
        ArrayList<Integer> ans = new ArrayList<>();
        for (int i : ansSet) {
            ans.add(i);
        }
        return ans;
    }
}