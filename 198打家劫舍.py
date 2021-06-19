class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):return 0
        elif (len(nums) == 1):return nums[0]
        maxRob = [nums[0],max(nums[0],nums[1])]
        for i in range(2,len(nums)):
            maxRob.append(max(maxRob[i - 2] + nums[i],maxRob[i - 1]))
        return maxRob[len(nums) - 1]

houses = [2,7,9,3,1]
mySolution = Solution()
print(mySolution.rob(houses))

