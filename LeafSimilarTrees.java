/*
    Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

    For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

    Two binary trees are considered leaf-similar if their leaf value sequence is the same.

    Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
*/

import java.util.ArrayList;

public class LeafSimilarTrees {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> t1 = new ArrayList<>();
        ArrayList<Integer> t2 = new ArrayList<>();
        dfs(root1, t1);
        dfs(root2, t2);
        return t1.equals(t2);
    }

    public void dfs(TreeNode node, ArrayList<Integer> values) {
        if (node != null) {
            if (node.left == null && node.right == null) {
                values.add(node.val);
            } else {
                dfs(node.left, values);
                dfs(node.right, values);
            }
        }
    }

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    
        TreeNode() {
        }
    
        TreeNode(int val) {
            this.val = val;
        }
    
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
}