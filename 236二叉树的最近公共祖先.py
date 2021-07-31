# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.found = False
        self.min = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.findmin(root, p, q)
        return self.min

    def findmin(self, root, p, q):
        if (root == None):
            return False

        find1 = self.findmin(root.left, p, q)
        if self.found: return True
        find2 = self.findmin(root.right, p, q)
        if self.found: return True
        foundHere = root.val == p.val or root.val == q.val

        if find1 and find2 or foundHere and find1 or foundHere and find2:
            self.min = root
            self.found = True
            return True
        if find1 or find2:
            return True
        if root.val == p.val or root.val == q.val:
            return True
