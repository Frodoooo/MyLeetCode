import random


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.myList = []
        self.mapping = {}

        for i in blacklist:
            self.mapping[i] = True

        for i in range(n):
            if i not in self.mapping.keys():
                self.myList.append(i)

    def pick(self) -> int:

        return self.myList[random.randint(0, len(self.myList))]