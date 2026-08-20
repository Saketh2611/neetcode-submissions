# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            lists = []
            if not root :
                return []
            if not root.left and not root.right :
                return [root.val]
            a = inorder(root.left)
            lists.append(root.val)
            b = inorder(root.right)
            return a + lists + b
        lists = inorder(root)
        return lists[k-1]

        