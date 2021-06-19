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
        res = self.dp(root)
        return max(res)

    def dp(self,root):
        if (root == None):return [0,0]
        left = self.dp(root.left)
        right = self.dp(root.right)
        do_it = root.val + left[0] + right[0]  #do_it表示抢时得到的最大钱数
        not_do = max(left) + max(right)       #not_do表示不抢root时得到的最大钱数
        return [not_do,do_it]

