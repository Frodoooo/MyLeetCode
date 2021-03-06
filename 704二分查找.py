class Solution(object):
    def search(self, nums, target):
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
                return mid
            elif(nums[mid] < target):
                left = mid + 1
            elif(nums[mid] > target):
                right = mid - 1

        return -1

nums = [-1,0,3,5,9,12]
target = 2
mySolution = Solution()
print(mySolution.search(nums,target))