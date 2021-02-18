public class maxDepth {
    public int maxDepth(Node root) {
        int currMax = 0;
        if (root == null) {
            return 0;
        }
        else if (root.children.size() == 0) {
            return 1;
        }
        for (Node n : root.children) {
            int depth = findDepth(n);
            if (depth > currMax) {
                currMax = depth;
            }
        }
        return 1 + currMax;
    }
    
    public int findDepth(Node root) {
        if (root.children.size() == 0) {
            return 1;
        }
        else {
            int currMax = 0;
            for (Node n : root.children) {
                int depth = findDepth(n);
                if (depth > currMax) {
                    currMax = depth;
                }
            }
            return 1 + currMax;
        }
    }
}