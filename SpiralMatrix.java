/*
Given an m x n matrix, return all elements of the matrix in spiral order.
*/

import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix {
    public List<Integer> spiralOrder(int[][] matrix) {
        boolean[][] seen = new boolean[matrix.length][matrix[0].length];
        ArrayList<Integer> ans = new ArrayList<>();
        int minRow = 0;
        int minCol = 0;
        int maxRow = matrix.length - 1; 
        int maxCol = matrix[0].length - 1;
        while (minRow <= maxRow && minCol <= maxCol) {
            int currX = minRow;
            int currY = minCol;
            while (currY <= maxCol && !seen[currX][currY]) {
                ans.add(matrix[currX][currY]);
                seen[currX][currY] = true;
                currY++;
            }
            currY = maxCol;
            currX++;
            minRow++;
            while (currX <= maxRow && !seen[currX][currY]) {
                ans.add(matrix[currX][currY]);
                seen[currX][currY] = true;
                currX++;
            }
            currX = maxRow;
            maxCol--;
            currY--;
            while (currY >= minCol && !seen[currX][currY]) {
                ans.add(matrix[currX][currY]);
                seen[currX][currY] = true;
                currY--;
            }
            currY = minCol;
            maxRow--;
            currX--;
            while (currX >= minRow && !seen[currX][currY]) {
                ans.add(matrix[currX][currY]);
                seen[currX][currY] = true;
                currX--;
            }
            currX = minRow;
            minCol++;
            currY++;
        }
        return ans;
    }
}