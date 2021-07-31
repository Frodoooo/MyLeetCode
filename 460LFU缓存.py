class DLinkedNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        self.freq = 1
class DoublyLinkedList:
    def __init__(self):
        self.head = DLinkedNode()
        self.tail = DLinkedNode()

    def isempty(self):
        if self.head.next.key == -1:
            return True
        else:
            return False

    def makeDLink(self):
        self.head.next = self.tail
        self.tail.pre = self.head

    def addNode(self,node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node
        node.next.pre = node

    def removeNode(self,node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def getOldest(self):
        node = self.tail.pre
        self.removeNode(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.freqMap = {} #储存每个频次对应的双向链表
        self.size = 0
        self.capacity = capacity
        self.min = 0 #储存当前最小频次


    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.freqInc(self.cache[key])
            return self.cache[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache.keys():
            self.freqInc(self.cache[key])
            self.cache[key].val = value
        else:
            self.addNode(DLinkedNode(key,value))


    def freqInc(self,node:DLinkedNode):
        #从原freq对应的链表移除，并更新self.min
        self.freqMap[node.freq].removeNode(node)  #从频次对应双向链表中移除该节点
        if self.freqMap[node.freq].isempty(): #若该双向链表清空
            self.freqMap.pop(node.freq)       #删除该频次
            if self.min == node.freq:        #若该频次为最小频次，则最小频次增加1
                self.min += 1
        node.freq += 1
        if node.freq not in self.freqMap.keys():
            self.freqMap[node.freq] = DoublyLinkedList()
            self.freqMap[node.freq].makeDLink()
        self.freqMap[node.freq].addNode(node)


    def addNode(self,node:DLinkedNode):
        if self.size == self.capacity:
            self.removeNode()
        self.cache[node.key] = node
        if 1 not in self.freqMap.keys():
            self.freqMap[1] = DoublyLinkedList()
            self.freqMap[1].makeDLink()
        self.freqMap[1].addNode(node)
        self.size += 1
        self.min = 1

    def removeNode(self):
        nodeToDelete = self.freqMap[self.min].getOldest()
        self.cache.pop(nodeToDelete.key)
        self.size -= 1

myLFU = LFUCache(2)
myLFU.put(1,1)
myLFU.put(2,2)
myLFU.get(1)
myLFU.put(3,3)
myLFU.get(2)
myLFU.get(3)
myLFU.put(4,4)
myLFU.get(1)
myLFU.get(3)
myLFU.get(4)
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)