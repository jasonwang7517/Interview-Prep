class Solution {
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