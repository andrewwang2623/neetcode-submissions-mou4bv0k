# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -1000000001, 1000000001)
    
    def helper(self, root, minimum, maximum):
        if root.val <= minimum or root.val >= maximum:
            return False
        if root.left is None:
            if root.right is None:
                return True
            else:
                return self.helper(root.right, root.val, maximum)
        else:
            if root.right is None:
                return self.helper(root.left, minimum, root.val)
            else:
                return self.helper(root.right, root.val, maximum) and self.helper(root.left, minimum, root.val)