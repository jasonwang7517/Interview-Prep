/*
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  
    - For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
*/

public class RemoveOuterParentheses {
    public String removeOuterParentheses(String S) {
        String str = "";
        char[] chars = S.toCharArray();
        int lPar = 1;
        int rPar = 0;
        for (int i = 1; i < chars.length; i++) {
            if (chars[i] == '(') {
                lPar += 1;
            }
            else if (chars[i] == ')') {
                rPar += 1;
            }
            if (lPar != rPar) {
                str += S.charAt(i);
            }
            else {
                lPar = 1;
                rPar = 0;
                i++;
            }
        }
        return str;
    }
}
