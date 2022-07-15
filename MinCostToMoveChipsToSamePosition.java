/*
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:
    - position[i] + 2 or position[i] - 2 with cost = 0.
    - position[i] + 1 or position[i] - 1 with cost = 1.

Return the minimum cost needed to move all the chips to the same position.
*/

public class MinCostToMoveChipsToSamePosition {
    public int minCostToMoveChips(int[] position) {
        int count0 = 0;
        int count1 = 0;
        if (position.length == 1) {
            return 0;
        }
        for (int i = 0; i < position.length; i++) {
            if (position[i] % 2 == 0) {
                count0++;
            }
            else if (position[i] % 2 == 1) {
                count1++;
                
            }
        }
        return Math.min(count0, count1);
    }
}