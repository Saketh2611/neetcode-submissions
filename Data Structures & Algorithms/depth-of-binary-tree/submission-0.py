class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0 
        if not root :
            return 0 
        if root.left is None and root.right is None :
            return 1 
        depth = 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        return depth