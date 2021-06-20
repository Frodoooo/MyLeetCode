class Solution:

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            if(i == 0 or (i > 0 and nums[i] != nums[i - 1])):
                target = -nums[i]
                target_supple = []
                left = i + 1
                right = len(nums) - 1
                while(left < right):
                    if(left > i + 1 and nums[left] == nums[left - 1]):
                        left += 1
                        continue
                    elif(nums[left] + nums[right]) == target:
                        target_supple.append([nums[left],nums[right]])
                        left += 1
                        right -= 1
                    elif (nums[left] + nums[right]) < target:
                        left += 1
                    else:
                        right -= 1

                for j in target_supple:
                    j.append(nums[i])
                    res.append(j)
        return res

nums = [0,0,0]

mySolution = Solution()
print(mySolution.threeSum(nums))