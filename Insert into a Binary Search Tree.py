# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root=TreeNode(val)
            return root
        def helper(node):
            if val<node.val:
                if node.left is None:
                    node.left=TreeNode(val)
                else:
                    helper(node.left)
            else:
                if node.right is None:
                    node.right=TreeNode(val)
                else:
                    helper(node.right)
        helper(root)
        return root
