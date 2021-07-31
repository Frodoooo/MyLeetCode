class DLinkedNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    # get：通过key查找内容，并提至队列头部，若不存在则返回-1
    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        else:
            findNode = self.cache[key]
            self.movetoHead(findNode)

            return findNode.val

    # put:添加或更新并放到队伍头部
    def put(self, key: int, val: int) -> None:
        if (key not in self.cache.keys()):
            newNode = DLinkedNode(key, val)
            self.cache[key] = newNode
            self.addtoHead(newNode)
        else:
            self.cache[key].val = val
            self.movetoHead(self.cache[key])

    def movetoHead(self, node):
        self.deleteNode(node)
        self.cache[node.key] = node
        self.addtoHead(node)

    # 添加节点至头部
    def addtoHead(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node
        node.next.pre = node
        self.size += 1
        if self.size > self.capacity:
            self.deleteNode(self.tail.pre)

    # 删除节点
    def deleteNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

        del self.cache[node.key]
        self.size -= 1


        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)