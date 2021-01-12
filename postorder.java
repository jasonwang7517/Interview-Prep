/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> postorder(Node root) {
        /*
        Recursive solution: 
        
        ArrayList<Integer> ans = new ArrayList<>();
        if (root == null) {
            return ans;
        }
        List<Node> childNodes = root.children;
        for (int i = 0; i < childNodes.size(); i++) {
            ans.addAll(postorder(childNodes.get(i)));
        }
        ans.add(root.val);
        return ans;
        */
        List<Integer> list = new ArrayList<>();
        if (root == null) return list;
        
        Stack<Node> stack = new Stack<>();
        stack.add(root);
        
        while(!stack.isEmpty()) {
            root = stack.pop();
            list.add(root.val);
            for(Node node: root.children)
                stack.add(node);
        }
        Collections.reverse(list);
        return list;
    }
}