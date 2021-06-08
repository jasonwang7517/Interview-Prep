class Solution(object):
    def inorderTraversal(self, root):
        ans = []
        if not root:
            return ans
        else:
            ans.extend(self.inorderTraversal(root.left))
            ans.append(root.val)
            ans.extend(self.inorderTraversal(root.right))
        return ans