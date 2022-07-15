/*
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
    - numberOfBoxesi is the number of boxes of type i.
    - numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.

You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
*/

import java.util.Arrays;

public class MaximumUnitsOnATruck {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a , b) -> -Integer.compare(a[1], b[1]));
        int maxUnits = 0;
        for(int[] box : boxTypes) {
            if(truckSize < box[0]) {
                return maxUnits + truckSize * box[1];
            }
            maxUnits += box[0] * box[1];
            truckSize -= box[0];
        }
        return maxUnits;
    }
}