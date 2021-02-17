class maxArea {
    public int maxArea(int[] height) {
        int currMax = Integer.MIN_VALUE;
        for (int i = 0; i < height.length - 1; i++) {
            for (int j = i + 1; j < height.length; j++) {
                int area = Math.min(height[i], height[j]) * Math.abs(i - j);
                if (area > currMax) {
                    currMax = area;
                }
            }
        }
        return currMax;
    }
}