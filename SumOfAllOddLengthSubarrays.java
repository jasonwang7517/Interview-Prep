/*
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
*/

class SumOfAllOddLengthSubarrays {
    public int sumOddLengthSubarrays(int[] arr) {
        int ans = 0;
        int subArraySize = 1;
        while (subArraySize <= arr.length) {
            for (int i = 0; i <= arr.length - subArraySize; i++) {
                for (int j = i; j < i + subArraySize; j++) {
                    ans += arr[j];
                }
            }
            subArraySize += 2;
        }
        return ans;
    }
}