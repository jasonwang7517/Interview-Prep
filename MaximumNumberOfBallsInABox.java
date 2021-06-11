/*
    You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of 
    boxes numbered from 1 to infinity.
    
    Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the 
    box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.

    Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.
*/

import java.util.HashMap;

public class MaximumNumberOfBallsInABox{
    public int countBalls(int lowLimit, int highLimit) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int i = lowLimit; i <= highLimit; i++) {
            int sum = 0;
            String s = Integer.toString(i);
            for (int j = 0; j < s.length(); j++) {
                sum += Character.getNumericValue(s.charAt(j));
            }
            if (hm.containsKey(sum)) {
                hm.put(sum, hm.get(sum) + 1);
            }
            else {
                hm.put(sum, 1);
            }
        }
        int currMax = 0;
        for (int i : hm.keySet()) {
            if (hm.get(i) > currMax) {
                currMax = hm.get(i);
            }
        }
        return currMax;
    }
}
