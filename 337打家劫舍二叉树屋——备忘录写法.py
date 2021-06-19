# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.memo = {}
    def rob(self,root):
        if (root == None): return 0
        if (root in self.memo.keys()): return self.memo[root]
        do_it = root.val + (0 if root.left == None else self.rob(root.left.left) + self.rob(root.left.right)) + \
                (0 if root.right == None else self.rob(root.right.left) +self.rob(root.right.right))
        not_do = self.rob(root.left) + self.rob(self,root.right)

        maxrob = max(do_it, not_do)
        self.memo[root] = maxrob
        return maxrob

