class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # 🔴 BASE CASE
        if not inorder:
            return None

        rv = preorder.pop(0)
        root = TreeNode(rv)

        i = 0
        while inorder[i] != rv:
            i += 1

        leftsub = self.buildTree(preorder, inorder[:i])
        rightsub = self.buildTree(preorder, inorder[i+1:])

        root.left = leftsub
        root.right = rightsub

        return root      # 🔴 YOU MISSED THIS
