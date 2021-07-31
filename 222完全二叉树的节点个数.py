# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if (root == None): return 0
        curLeft = root
        curRight = root
        hleft = 0
        hright = 0
        while (curLeft):
            curLeft = curLeft.left
            hleft += 1

        while (curRight):
            curRight = curRight.right
            hright += 1

        print([hleft, hright])

        if (hleft == hright):
            print(hleft * hleft - 1)
            return math.pow(2,hleft) - 1
        else:
            print('enter next')
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
