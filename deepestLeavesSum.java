/*
Given a binary tree, return the sum of values of its deepest leaves.
*/

import java.util.LinkedList;
import java.util.Queue;

class DeepestLeavesSum {
    public class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
  }

    public int deepestLeavesSum(TreeNode root) {
        int max = 0;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            max = 0;
            int size = queue.size();
            while(size-- > 0) {
                TreeNode curr = queue.remove();
                max += curr.val;
                if (curr.left != null) {
                    queue.offer(curr.left);
                }
                if (curr.right != null){
                    queue.offer(curr.right);
                }   
            }   
        }
        return max;
    }
}
