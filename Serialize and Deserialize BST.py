# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        self.data=""
        def bst(node):
            if node is None:
                return
            self.data+=str(node.val)+" "
            bst(node.left)
            bst(node.right)
        bst(root)
        return self.data[:len(self.data)-1]

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if len(data)==0:
            return None
        data=list(map(int,data.split(' ')))
        root=TreeNode(data[0])
        
        def bst(i,node):
            if data[i]<node.val:
                if node.left is None:
                    node.left=TreeNode(data[i])
                    return
                bst(i,node.left)
            else:
                if node.right is None:
                    node.right=TreeNode(data[i])
                    return
                bst(i,node.right)
        for i in range(1,len(data)):
            bst(i,root)
            
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
