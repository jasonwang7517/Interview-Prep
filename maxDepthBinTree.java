/*

*/

public class maxDepthBinTree {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(findDepth(root.left), findDepth(root.right));
    }
    
    public int findDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        else if (root.left == null && root.right == null) {
            return 1;
        }
        else if (root.left == null && root.right != null) {
            return 1 + findDepth(root.right);
        }
        else if (root.left != null && root.right == null) {
            return 1 + findDepth(root.left);
        }
        else {
            return 1 + Math.max(findDepth(root.left), findDepth(root.right));
        }
    }
}
