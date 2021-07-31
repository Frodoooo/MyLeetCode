class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stacks = []
        nextGreaterDict = {}
        for i in range(len(nums2)):
            while stacks :
                if nums2[i] > stacks[-1]:
                    nextGreaterDict[stacks.pop(-1)] = nums2[i]
                else:
                    stacks.append(nums2[i])
                    break
            if not stacks:
                stacks.append(nums2[i])

        res = []
        for i in nums1:
            if i in nextGreaterDict.keys():
                res.append(nextGreaterDict[i])
            else:
                res.append(-1)
        return res


