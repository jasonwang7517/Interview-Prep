/*
    You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces
    are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not
    allowed to reorder the integers in each array pieces[i].

    Return true if it is possible to form the array arr from pieces. Otherwise, return false.

    Constraints:
        - 1 <= pieces.length <= arr.length <= 100
        - sum(pieces[i].length) == arr.length
        - 1 <= pieces[i].length <= arr.length
        - 1 <= arr[i], pieces[i][j] <= 100
        - The integers in arr are distinct.
        - The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
 */
class canFormArray {
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