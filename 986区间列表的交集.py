class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i,j = 0,0 #双指针
        res = []
        while(i < len(firstList) and j < len(secondList)):
            left1,right1 = firstList[i]
            left2,right2 = secondList[j]
            if right2 < left1:
                j += 1
            elif right1 < left2:
                i += 1
            else:
                res.append([max(left1,left2),min(right1,right2)])
                if(right1 < right2):
                    i += 1
                else:
                    j += 1
        return res


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
mySolution = Solution()
print(mySolution.intervalIntersection(firstList,secondList))
