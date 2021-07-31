import collections

class Solution:
    def maxSlidingWindow(self, nums, k):

        deque = collections.deque([])
        res = []
        max = nums[0]
        for i in range(len(nums)):

            while deque:
                if nums[i] > deque[-1]:
                    deque.pop()
                else:
                    deque.append(nums[i])
                    break
            if not deque:
                deque.append(nums[i])
            if i < k - 1:
                continue

            res.append(deque[0])
            if deque[0] == nums[i - k + 1]:
                deque.popleft()
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
mySolution = Solution()
print(mySolution.maxSlidingWindow(nums,k))