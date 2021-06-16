class Solution(object):
    def __init__(self):
        self.output = []
        self.track = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.tracking(nums)

        return self.output

    def tracking(self,nums):
        if len(nums)==0:
            self.output.append(self.track[:])
        else:
            for i in range(len(nums)):
                a = nums.pop(i)
                self.track.append(a)
                self.tracking(nums)
                self.track.pop()
                nums.insert(i,a)

nums = [1,2,3]
mySolution = Solution()
output = mySolution.permute(nums)
print(output)