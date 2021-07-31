class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        f = {}

        # 寻找或设置x的族类
        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        # 将y整族并到x的族类
        def union(x, y):
            f[find(y)] = find(x)

        if not board or not board[0]:
            return

        row = len(board)
        col = len(board[0])

        dummy = row * col  # 绝不属于当前下标的族类，将边缘的"O"归到这一类

        for i in range(row):
            for j in (0,col - 1):
                if board[i][j] == "O":
                    union(dummy,i*col + j)

        for j in range(col):
            for i in (0,row - 1):
                if board[i][j] == "O":
                    union(dummy,i*col + j)

        print(f)

        for i in range(1,row - 1):
            for j in range(1,col - 1):
                if board[i][j] == "O":
                    for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        if board[i + x][j + y] == 'O':
                            union((i + x) * col + (j + y), i * col + j)
                            print([x,y])
                            print(f)

        print("out")
        print([dummy, find(dummy)])
        print(f)
        for i in range(row):
            for j in range(col):
                if (find(dummy) == find(i * col + j)):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        print(f)

board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
mySolution = Solution()
mySolution.solve(board)
print(board)