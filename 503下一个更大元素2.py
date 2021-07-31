class Solution:
    def nextGreaterElements(self,nums2):
        stacks = []
        res = [-1 for i in range(len(nums2))]
        n = len(nums2)
        for i in range(2 * n):
            index = i % n
            while stacks :
                if nums2[i % n] > nums2[stacks[-1]]:
                    res[stacks.pop()] = nums2[i % n]
                else:
                    stacks.append(i % n)
                    break
            if not stacks:
                stacks.append(i % n)

        return res

temperatures = [1,2,3,4,5]
my = Solution()
print(my.nextGreaterElements(temperatures))
