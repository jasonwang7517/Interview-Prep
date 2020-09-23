import java.util.ArrayList;
import java.util.List;

public class mergeArrays {
    public static List<Integer> mergeArrays(List<Integer> a, List<Integer> b) {
        // Write your code here
        ArrayList<Integer> ans = new ArrayList<>();
        int aPointer = 0;
        int bPointer = 0;
        while (ans.size() != a.size() + b.size() && aPointer < a.size() && bPointer < b.size()) {
            if (a.get(aPointer) <= b.get(bPointer)) {
                ans.add(a.get(aPointer));
                aPointer++;
            }
            else {
                ans.add(b.get(bPointer));
                bPointer++;
            }
        }
        while (aPointer < a.size()) {
            ans.add(a.get(aPointer));
            aPointer++;
        }
        while (bPointer < b.size()) {
            ans.add(b.get(bPointer));
            bPointer++;
        }
        return ans;
    }
}
