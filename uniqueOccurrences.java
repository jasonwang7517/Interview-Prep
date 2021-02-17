import java.util.HashMap;
import java.util.HashSet;

class uniqueOccurrences {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        HashSet<Integer> freq = new HashSet<>();
        for (int i : arr) {
            if (map.containsKey(i)) {
                map.put(i, map.get(i) + 1);
            }
            else {
                map.put(i, 1);
            }
        }
        for (int i : map.keySet()) {
            if (freq.contains(map.get(i))) {
                return false;
            }
            else {
                freq.add(map.get(i));
            }
        }
        return true;
    }
}