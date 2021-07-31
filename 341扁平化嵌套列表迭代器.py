#提前展平，队列写法
'''class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = []
        self.dfs(nestedList)

    def dfs(self,nestedList):
        for i in nestedList:
            if i.isInteger():
                self.queue.append(i.getInteger)
            else:
                self.dfs(i.getList())

    def next(self) -> int:
        cur = self.queue.pop(0)
        return cur.getInteger()

    def hasNext(self) -> bool:
        return len(self.queue)
    # Your NestedIterator object will be instantiated and called as such:
    # i, v = NestedIterator(nestedList), []
    # while i.hasNext(): v.append(i.next())'''

#栈写法，判断hasnext时展平

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for i in range(len(nestedList) - 1,-1,-1):
            self.stack.append(i.getList())
    def next(self) -> int:
        return self.stack.pop(-1)
    def hasNext(self) -> bool:
        while (len(self.stack)):
            if(self.stack[-1].isInteger()):
                return self.stack.pop(-1)
    # Your NestedIterator object will be instantiated and called as such:
    # i, v = NestedIterator(nestedList), []
    # while i.hasNext(): v.append(i.next())