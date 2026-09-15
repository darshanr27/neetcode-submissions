# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = { v:i for i, v in enumerate(inorder)} # Hash inorder
        self.pre = 0 # preorder pointer

        def build(left, right):
            if left > right: return None

            root = TreeNode(preorder[self.pre])
            self.pre += 1
            mid = inorderIdx[root.val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)        