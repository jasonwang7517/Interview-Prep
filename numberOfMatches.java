class numberOfMatches {
    public int numberOfMatches(int n) {
        int ans = 0;
        while (n > 1) {
            ans += n / 2;
            if (n % 2 == 0) {
                n = n / 2;
            }
            else {
                n = 1 + (n / 2);
            }
        }
        return ans;
    }
}