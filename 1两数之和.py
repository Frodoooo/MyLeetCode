class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic_to_num = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dic_to_num.keys():
                return [i, dic_to_num[target - nums[i]]]
            dic_to_num[nums[i]] = i
        return []

"""class Solution(object):
    def twoSum(self, nums, target):
       
        dic_to_num = {}
        for i in range(len(nums)):
            dic_to_num[nums[i]] = []
        for i in range(len(nums)):
            dic_to_num[nums[i]].append(i)
        for i in range(len(nums)):
            if ((target - nums[i]) in dic_to_num.keys()):
                first = dic_to_num[nums[i]].pop()
                if(len(dic_to_num[target - nums[i]]) > 0):
                    return [first, dic_to_num[target - nums[i]].pop()]
        return []"""


nums = [3,3]
target = 6
mySolution = Solution()
print(mySolution.twoSum(nums,target))