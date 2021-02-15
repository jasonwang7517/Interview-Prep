/*
    You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

    Return the sum of all the unique elements of nums.

    Constraints:
        - 1 <= nums.length <= 100
        - 1 <= nums[i] <= 100
*/

class sumOfUnique {
    public int sumOfUnique(int[] nums) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        int ans = 0;
        for (int i : nums){
            if (!hm.containsKey(i)) {
                hm.put(i, 1);
            }
            else {
                hm.put(i, hm.get(i) + 1);
            }
        }
        for (int i : hm.keySet()) {
            if (hm.get(i) == 1) {
                ans += i;
            }
        }
        return ans;
    }
}