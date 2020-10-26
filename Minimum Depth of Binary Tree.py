# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        def height(node,h):
            if node.left is None and node.right is None:
                return h
            elif node.left and node.right:
                return min(height(node.left,h+1),height(node.right,h+1))
            elif node.left:
                return height(node.left,h+1)
            else:
                return height(node.right,h+1)
        
        return height(root,1)
