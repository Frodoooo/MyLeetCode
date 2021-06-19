class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals = sorted(intervals,key=lambda x:(x[0],-x[1]))
        covered = 0
        left = intervals[0][0]
        right = intervals[0][1]
        for interval in intervals[1:]:
            nextLeft = interval[0]
            nextRight = interval[1]
            #分三个情况
            #case1：覆盖了下一个区间 ->covered加一
            if(right >= nextRight):
                covered += 1

            #case2:部分重叠 -> 合并
            elif(right >= nextLeft and right < nextRight):
                right = nextRight

            #case3: 完全不相交：更新起终点
            elif(right < nextLeft):
                left = nextLeft
                right = nextRight

        return len(intervals) - covered

intervals = [[1,4],[3,6],[2,8]]
mySolution = Solution()
print(mySolution.removeCoveredIntervals(intervals))