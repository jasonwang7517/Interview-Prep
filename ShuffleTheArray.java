/*
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
*/

public class ShuffleTheArray {
    public int[] shuffle(int[] nums, int n) {
        int[] shuffledArr = new int[nums.length];
        for (int i = 0; i < shuffledArr.length - 1; i += 2){
            shuffledArr[i] = nums[i / 2];
            shuffledArr[i+1] = nums[(i / 2) + n];
        }
        return shuffledArr;
    }
}
