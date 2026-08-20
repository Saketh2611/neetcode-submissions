class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            # Both nodes are smaller → go left
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            # Both nodes are greater → go right
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            # Split point → this is LCA
            else:
                return curr
