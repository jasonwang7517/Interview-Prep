/*
    Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
*/

import java.util.HashSet;
import java.util.Set;

public class Intersection {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> s = new HashSet<>();
        Set<Integer> s2 = new HashSet<>();
        Set<Integer> s3 = new HashSet<>();
        for (int i : nums1) {
            s.add(i);
        }
        for (int i : nums2) {
            s2.add(i);
        }
        for (int i : s) {
            if (s2.contains(i)) {
                s3.add(i);
            }
        }

        int[] ans = new int[s3.size()];
        int index = 0;
        for (int i : s3) {
            ans[index] = i;
            index++;
        }
        return ans;
    }
}