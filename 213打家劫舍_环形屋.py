class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):return 0
        elif (len(nums) <= 3):return max(nums)

        nums1 = nums[0:len(nums)-1]
        nums2 = nums[1:len(nums)]
        maxRob1 = [nums1[0],max(nums1[0],nums1[1])]
        maxRob2 = [nums2[0], max(nums2[0], nums2[1])]
        for i in range(2,len(nums1)):
            maxRob1.append(max(maxRob1[i - 2] + nums1[i],maxRob1[i - 1]))

        for i in range(2,len(nums2)):
            maxRob2.append(max(maxRob2[i - 2] + nums2[i],maxRob2[i - 1]))
        return max(maxRob1[len(nums1) - 1],maxRob2[len(nums2) - 1])

houses = [1,2,3,1]
mySolution = Solution()
print(mySolution.rob(houses))
