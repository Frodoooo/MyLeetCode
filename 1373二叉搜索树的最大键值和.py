# 若节点的参数取决于其子树，利用后序遍历会很方便
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sums = []

    def maxSumBST(self, root: TreeNode) -> int:
        self.traverse(root)
        return max(self.sums)

    def traverse(self, root):
        if (not root):
            return [True, 999999, -999999, 0]
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        if (left[0] and right[0]):
            if (left[2] < root.val and right[1] > root.val):
                mysum = left[3] + right[3] + root.val
                mymin = min(left[1], root.val)
                mymax = max(right[2], root.val)
                self.sums.append(mysum)
                return [True, mymin, mymax, mysum]

        return [False, 999999, -999999, 0]
