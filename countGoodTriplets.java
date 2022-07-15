/*
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
    - 0 <= i < j < k < arr.length
    - |arr[i] - arr[j]| <= a
    - |arr[j] - arr[k]| <= b
    - |arr[i] - arr[k]| <= c
    - Where |x| denotes the absolute value of x.

Return the number of good triplets.
*/
import static java.lang.Math.*;

public class CountGoodTriplets {
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
        int triplets = 0;
        for (int i = 0; i < arr.length - 2; i++) {
            for (int j = i + 1; j < arr.length - 1; j++) {
                for (int k = j + 1; k < arr.length; k++) {
                    if (abs(arr[i] - arr[j]) <= a && abs(arr[j] - arr[k]) <= b && abs(arr[i] - arr[k]) <= c) {
                        triplets++;
                    }
                }
            }
        }
        return triplets;
    }
}
