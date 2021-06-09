import java.util.ArrayList;

class RecentCounter {
    ArrayList<Integer> requests;

    public RecentCounter() {
        requests = new ArrayList<>();
    }
    
    public int ping(int t) {
        requests.add(t);
        int ans = 0;
        int min = t - 3000;
        int max = t;
        for (int i : requests) {
            if (i >= min && i <= max) {
                ans++;
            }
        }
        return ans;
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */