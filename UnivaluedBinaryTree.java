public class UnivaluedBinaryTree {
    public boolean isUnivalTree(TreeNode root) {
        if (root == null || (root.left == null && root.right == null)) {
            return true;
        }
        else if (root.left == null && root.right != null) {
            return root.val == root.right.val && isUnivalTree(root.right);
        }
        else if (root.left != null && root.right == null) {
            return root.val == root.left.val && isUnivalTree(root.left);
        }
        else {
            return root.val == root.left.val && root.val == root.right.val && isUnivalTree(root.left) && isUnivalTree(root.right);
        }
    }

    class TreeNode {
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
}