/**
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all 
of them with no order requirement. You could assume there always exists an answer.
*/

import java.util.HashMap;
import java.util.ArrayList;

class MinimumIndexSumOfTwoLists {
    public String[] findRestaurant(String[] list1, String[] list2) {
        HashMap<String, Integer> map1 = new HashMap<>();
        for (int i = 0; i < list1.length; i++) {
            map1.put(list1[i], i);
        }
        HashMap<String, Integer> map2 = new HashMap<>();
        for (int i = 0; i < list2.length; i++) {
            map2.put(list2[i], i);
        }
        int ans = Integer.MAX_VALUE;
        ArrayList<String> words = new ArrayList<>();
        for (String s : map1.keySet()) {
            if (map2.containsKey(s)) {
                int curr = map1.get(s) + map2.get(s);
                if (curr == ans) {
                    words.add(s); 
                }
                else if (curr < ans) {
                    ArrayList<String> newWord = new ArrayList<>();
                    newWord.add(s);
                    words = newWord;
                    ans = curr;
                }
            }
        }
        String[] stringArray = words.toArray(new String[0]);
        return stringArray;
    }
}