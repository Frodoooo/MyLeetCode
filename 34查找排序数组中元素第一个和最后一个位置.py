class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while(left <= right):
            mid = int(left + (right - left)/2)
            if (nums[mid] == target):
                right = mid - 1
            elif(nums[mid] < target):
                left = mid + 1
            elif(nums[mid] > target):
                right = mid - 1

        if(left >= len(nums)): leftOut = -1
        elif (nums[left] == target):
            leftOut = left
        else: leftOut = -1
##################################
        left = 0
        right = len(nums) - 1

        while(left <= right):
            mid = int(left + (right - left)/2)
            if (nums[mid] == target):
                left = mid + 1
            elif (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1

        if(right < 0):
            rightOut = -1
        elif(nums[right] == target):
            rightOut = right
        else:
            rightOut = -1

        return [leftOut,rightOut]

nums = [1]
target = 1
mySolution = Solution()
print(mySolution.searchRange(nums,target))