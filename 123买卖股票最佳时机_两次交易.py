import numpy
class Solution(object):
    def maxProfit(self,prices,max_k = 2):
        """
        :type max_k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dptable = numpy.zeros((n,max_k+1,2),int)
        for i in range(n):
            for k in range(max_k,0,-1):
                if( i == 0):

                    dptable[i][k][1] = -prices[i]
                    continue
                dptable[i][k][0] = max(dptable[i - 1][k][0], dptable[i - 1][k][1] + prices[i])
                dptable[i][k][1] = max(dptable[i - 1][k][1],dptable[i - 1][k- 1][0] - prices[i])

        return dptable[n - 1][max_k][0]


prices = [3,3,5,0,0,3,1,4]

mySolution = Solution()
print(mySolution.maxProfit(prices))