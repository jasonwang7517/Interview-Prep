class peakIndexInMountainArray {
    public int peakIndexInMountainArray(int[] arr) {
        int ans = 0;
        for (int i = 1; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                ans = i;
                return ans;
            }
        }
        return ans;
    }
}