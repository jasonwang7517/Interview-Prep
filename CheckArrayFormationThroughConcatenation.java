/*
You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. 

Your goal is to form arr by concatenating the arrays in pieces in any order. 

However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.
*/
public class CheckArrayFormationThroughConcatenation {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        StringBuilder sb = new StringBuilder();
        for(int x : arr){
            sb.append(x);
            sb.append("#");
        }
        for(int i = 0; i < pieces.length; i++){
            StringBuilder res = new StringBuilder();
            for(int j = 0; j < pieces[i].length; j++){
                res.append(String.valueOf(pieces[i][j]));
                res.append("#");
            }
            if(!sb.toString().contains(res.toString())){
                return false;
            }
        }
        return true;
    }
}