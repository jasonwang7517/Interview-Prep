class Solution {
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
                if(curr.left != null) {
                    queue.offer(curr.left);
                }
                if(curr.right != null){
                queue.offer(curr.right);
                }   
            }   
        }
        return max;
    }
}
