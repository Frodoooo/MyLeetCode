import collections

class Solution:
    def advantageCount(self, nums1:list, nums2:list):

        nums1.sort(reverse = True)
        nums1 = collections.deque(nums1)
        nums2sorted = [[i,nums2[i]] for i in range(len(nums2))]
        nums2sorted.sort(key=lambda x:x[1],reverse= True)
        res = []
        B2A = {}

        while nums1:
            if nums1[0] > nums2sorted[0][1]:
                B2A[nums2sorted.popleft()] = nums1.popleft()

            else:
                B2A[nums2sorted.popleft()] = nums1.pop()

        for i in nums2:
            res.append(B2A[[i,nums2[i]]])

        return res


