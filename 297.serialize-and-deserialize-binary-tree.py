#
# @lc app=leetcode id=297 lang=python
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = list()
        def get_string(root):
            if root == None:
                res.append(None)
            else:
                res.append(root.val)
                get_string(root.left)
                get_string(root.right)
            

        get_string(root)
        return res
        
          
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if data:
            cur = data.pop(0)
            if cur == None:
                return None
            root = TreeNode(cur)
            root.left = self.deserialize(data)
            root.right = self.deserialize(data)
            return root
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
