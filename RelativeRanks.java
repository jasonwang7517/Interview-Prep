/**
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. 
The placement of each athlete determines their rank:

- The 1st place athlete's rank is "Gold Medal".
- The 2nd place athlete's rank is "Silver Medal".
- The 3rd place athlete's rank is "Bronze Medal".
- For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.
 */

class RelativeRanks {
    public String[] findRelativeRanks(int[] score) {
        ArrayList<Integer> scoreCopy = new ArrayList<>();
        String[] ans = new String[score.length];
        for (int i = 0; i < score.length; i++) {
            scoreCopy.add(score[i]);
        }
        Collections.sort(scoreCopy, Collections.reverseOrder());
        HashMap<Integer, Integer> places = new HashMap<>();
        for (int i = 0; i < scoreCopy.size(); i++) {
            places.put(scoreCopy.get(i), i);
        }
        for (int i = 0; i < ans.length; i++) {
            int val = score[i];
            int place = places.get(val) + 1;
            if (place == 1) {
                ans[i] = "Gold Medal";
            }
            else if (place == 2) {
                ans[i] = "Silver Medal";
            }
            else if (place == 3) {
                ans[i] = "Bronze Medal";
            }
            else {
                ans[i] = Integer.toString(place);
            }
        }
        return ans;
    }
}