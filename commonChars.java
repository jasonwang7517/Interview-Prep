import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class commonChars {
    public List<String> commonChars(String[] A) {
        List<String> ans = new ArrayList<>();
        int[] count = new int[26]; 
        Arrays.fill(count, Integer.MAX_VALUE);
        for (String str : A) {
            int[] cnt = new int[26];
            for (char c : str.toCharArray()) {
                int index = c - 'a';
                cnt[index] += 1;
            }
            for (int i = 0; i < 26; ++i) { 
                count[i] = Math.min(cnt[i], count[i]); 
            } 
        }
        for (char c = 'a'; c <= 'z'; ++c) {
            while (count[c - 'a']-- > 0) { 
                ans.add("" + c); 
            }
        }
        return ans;
    }
}
