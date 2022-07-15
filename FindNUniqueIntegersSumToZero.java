/*
Given an integer n, return any array containing n unique integers such that they add up to 0.
*/

public class FindNUniqueIntegersSumToZero {
    public static int[] sumZero(int n) {
        int[] ans = new int[n];
        int currElements = 0;
        int currVal = n;
        int currIndex = 0;
        if (n % 2 == 0) {
            while (currElements < n) {
                ans[currIndex] = currVal;
                ans[currIndex + 1] = -currVal;
                currIndex += 2;
                currVal--;
                currElements += 2;
            }
        }
        else if (n % 2 == 1) {
            while (currElements < n - 1) {
                ans[currIndex] = currVal;
                ans[currIndex + 1] = -currVal;
                currIndex += 2;
                currVal--;
                currElements += 2;
            }
        }
        return ans;
    }
}
