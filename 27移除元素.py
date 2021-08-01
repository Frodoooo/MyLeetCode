class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        fast = 0
        while fast < len(nums) :
            while nums[fast] == val :
                fast += 1
            nums[slow] = nums[fast]
            fast += 1
        return slow + 1