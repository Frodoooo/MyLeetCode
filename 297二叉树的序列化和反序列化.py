class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s = ""
        queue = []
        queue.append(root)
        while queue:
            root = queue.pop(0)
            if root:
                s += str(root.val)
                queue.append(root.left)
                queue.append(root.right)
            else:
                s += "n"
            s += " "
        return s
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


        # Your Codec object will be instantiated and called as such:
        # ser = Codec()
        # deser = Codec()
        # ans = deser.deserialize(ser.serialize(root))
        tree = data.split()
        print(tree)
        if(tree[0] == "n"):
            return None
        queue = []
        root = TreeNode(tree[0])

        queue.append(root)
        i = 1
        while queue:
            cur = queue.pop(0)
            if cur == None:
                break
            cur.left = TreeNode(int(tree[i])) if tree[i] != "n" else None
            cur.right = TreeNode(int(tree[i+1])) if tree[i+1] != "n" else None
            i += 2
            queue.append(cur.left)
            queue.append(cur.right)

        return root