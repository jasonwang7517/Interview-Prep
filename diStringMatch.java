/*
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
    - s[i] == 'I' if perm[i] < perm[i + 1], and
    - s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.
*/

public class DIStringMatch {
    public int[] diStringMatch(String S) {
        int[] ans = new int[S.length() + 1];
        int min = 0;
        int max = S.length();
        if (S.charAt(0) == 'I'){
            ans[0] = min;
            min++;
        }
        else {
            ans[0] = max;
            max--;
        }
        for (int i = 1; i < S.length(); i++) {
            if (S.charAt(i) == 'I') {
                ans[i] = min;
                min++;
            }
            else if (S.charAt(i) == 'D') {
                ans[i] = max;
                max--;
            }
        }
        if (S.charAt(S.length() - 1) == 'I'){
            ans[ans.length - 1] = min;
        }
        else {
            ans[ans.length - 1] = max;
        }
        return ans;
    }
}