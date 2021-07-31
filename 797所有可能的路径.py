class Solution:
    def __init__(self):
        self.res = []
        self.len = 0
    def allPathsSourceTarget(self, graph):
        path = []
        self.len = len(graph)
        self.traverse(graph,0,path)
        return self.res

    def traverse(self,graph,index,path):
        path.append(index)
        if(index == self.len - 1):
            self.res.append(path[:])
        else:
            for i in graph[index]:
                self.traverse(graph,i,path)
        path.pop(-1)