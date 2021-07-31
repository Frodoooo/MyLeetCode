class Solution:
    def dailyTemperatures(self, temperatures):
        if not temperatures:
            return []
        stacks = []
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stacks:
                if temperatures[i] > temperatures[stacks[-1]]:
                    res[stacks[-1]] = i - stacks[-1]
                    stacks.pop()
                else:
                    stacks.append(i)
                    break
            if not stacks:
                stacks.append(i)

        return res

temperatures = [73,74,75,71,69,72,76,73]
my = Solution()
print(my.dailyTemperatures(temperatures))