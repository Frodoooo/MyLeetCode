class Solution(object):
    def minDepth(self, root):
        if(root == None):return 0
        q = []
        q.append(root)
        depth = 1
        while(len(q)>0):
            size = len(q)
            for i in range(size):
                cur = q.pop(0)
                if (cur.left==None and cur.right==None):
                    return depth
                if (cur.left):
                    q.append(cur.left)
                if (cur.right):
                    q.append(cur.right)
            depth += 1
        return depth
