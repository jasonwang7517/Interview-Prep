public class NumberOfStepsToReduceToZero {
/*
    Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even,
    you have to divide it by 2, otherwise, you have to subtract 1 from it.
*/
    public int numberOfSteps (int num) {
        int input = num;
        int steps = 0;
        while (true) {
            if (input == 0) {
                return steps;
            }
            else if (input % 2 == 0) {
                input = input / 2;
                steps++;
            }
            else {
                input -= 1;
                steps++;
            }
        }
    }
}
