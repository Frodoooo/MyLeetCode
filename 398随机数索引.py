import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        i = 1
        for j in len(self.nums):
            if self.nums[j] == target:
                rand = random.randint(1,i)
                if rand == 1:
                    resultIndex = j
                i += 1
        return resultIndex


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)