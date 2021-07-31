class Solution:
    def equationsPossible(self, equations):
        f = {}

        def find(x):
            f.setdefault(x,x)
            if(f[x] != x):
                f[x] = find(f[x])
            return f[x]

        def union(x,y):
            f[find(y)] = find(x)

        for equation in equations:
            print(equation)
            if equation[1] == '=':
                union(equation[0],equation[3])

        for equation in equations:
            if equation[1] == '!':
                if find(equation[0]) == find(equation[3]):
                    return False

        return True


board = ["a==b","b!=a"]
mySolution = Solution()
print(mySolution.equationsPossible(board))