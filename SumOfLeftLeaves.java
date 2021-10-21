/**
Given the root of a binary tree, return the sum of all left leaves.
 */

 /**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class SumOfLeftLeaves {
    public int sumOfLeftLeaves(TreeNode root) {
        int ans = 0;
        if (root == null) {
            return 0;
        }
        if (isLeaf(root.left)) {
            ans += root.left.val;
        }
        else {
            ans += sumOfLeftLeaves(root.left);
        }
        if (!isLeaf(root.right)) {
            ans += sumOfLeftLeaves(root.right);
        }
        return ans;
    }
    
    public boolean isLeaf(TreeNode curr) {
        if (curr == null) {
            return false;
        }
        return curr.left == null && curr.right == null;
    }
}