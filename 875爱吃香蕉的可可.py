class Solution:
    def minEatingSpeed(self, piles: list, h: int) -> int:
        left = 1
        right = 30
        while(left <= right):
            mid = int(left + (right - left)/2)
            if(self.f(piles,mid) > h):
                left = mid + 1
            else:
                right = mid - 1

        return left


    def f(self,myList,k):
        hours = 0
        for i in myList:
            hours += int(i/k)
            if i % k != 0:
                hours += 1
        return hours

mine = Solution()
print(mine.minEatingSpeed([30,11,23,4,20],6))