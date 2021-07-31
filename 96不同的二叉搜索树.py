class Solution:
    def __init__(self):
        self.results = []

    def numTrees(self, n: int) -> int:
        for i in range(n + 1):
            self.results.append(0)
        print(self.results)
        return self.count(n)

    def count(self,n):
        if(self.results[n] != 0):
            return self.results[n]
        elif(n == 0 or n == 1):
            print("0 this time")
            self.results[n] = 1
            return 1
        res = 0
        for i in range(n):
            res += self.count(i) * self.count(n - i - 1)
        self.results[n] = res
        return res

n = 3
mySolution =Solution()
print(mySolution.numTrees(n))