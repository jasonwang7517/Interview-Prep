import java.util.LinkedList;
import java.util.Queue;

public class rangeSumBST {
    /*
     * Definition for a binary tree node.
     */
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

    class Solution {
        public int rangeSumBST(TreeNode root, int L, int R) {
            int ans = 0;
            if (root.val >= L && root.val <= R) {
                ans += root.val;
            }
            if (root.left != null) {
                ans += rangeSumBST(root.left, L, R);
            }
            if (root.right != null) {
                ans += rangeSumBST(root.right, L, R);
            }
            return ans;
        }

        public int rangeSumBFS(TreeNode root, int L, int R) {
            int ans = 0;
            Queue<TreeNode> q = new LinkedList<>();
            if (root.val >= L && root.val <= R) {
                ans += root.val;
            }
            q.add(root.left);
            q.add(root.right);
            while (!q.isEmpty()) {
                TreeNode curr = q.remove();
                if (curr.val >= L && curr.val >= R) {
                    ans += curr.val;
                }
                q.add(curr.left);
                q.add(curr.right);
            }
            return ans;
        }
    }
}
