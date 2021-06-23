class Solution:

    def threeSum(self, nums, bigtarget):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            if(i == 0 or (i > 0 and nums[i] != nums[i - 1])):
                target = bigtarget - nums[i]
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

    def fourSum(self, nums, bigtarget):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            target = bigtarget - nums[i]
            three = self.threeSum(nums[i + 1: ], target)
            for j in three:
                j.append(nums[i])
                res.append(j)
        return res

nums = [5,5,3,5,1,-5,1,-2]
target = 4

mySolution = Solution()
print(mySolution.fourSum(nums,target))