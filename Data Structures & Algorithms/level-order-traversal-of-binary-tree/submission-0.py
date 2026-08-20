# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        queue = [root]
        ans = []
        while queue:
            level_nodes = []
            for _ in range(len(queue)) :
                node = queue.pop(0)
                if node.left :
                    queue.append(node.left)
                if node.right : 
                    queue.append(node.right)
                level_nodes.append(node.val)
            ans.append(level_nodes)
        return ans 







        