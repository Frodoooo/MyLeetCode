class FreqStack:

    def __init__(self):
        self.val2freq = {}
        self.freq2val = {}
        self.max = 0
    def push(self, val: int) -> None:
        if val in self.val2freq.keys():
            self.val2freq[val] += 1
            if self.val2freq[val] not in self.freq2val.keys():
                self.freq2val[self.freq2val[val]] = [val]
            else:
                self.freq2val[self.freq2val[val]].append(val)
        else:
            self.val2freq[val] = 1
        self.max = max(self.val2freq[val],self.max)

    def pop(self) -> int:
        result = self.freq2val[self.max].pop(-1)
        if not self.freq2val[self.max]:
            self.freq2val.pop(self.max)
            self.max -= 1
        return result



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()