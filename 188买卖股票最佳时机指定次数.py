import numpy
class Solution(object):
    def maxProfit(self,max_k,prices):
        """
        :type max_k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n==0:return 0
        dptable = numpy.zeros((n,max_k+1,2),int)
        for i in range(n):
            for k in range(max_k,0,-1):
                if( i == 0):

                    dptable[i][k][1] = -prices[i]
                    continue
                dptable[i][k][0] = max(dptable[i - 1][k][0], dptable[i - 1][k][1] + prices[i])
                dptable[i][k][1] = max(dptable[i - 1][k][1],dptable[i - 1][k- 1][0] - prices[i])

        return dptable[n - 1][max_k][0]

prices = []
k = 2

mySolution = Solution()
print(mySolution.maxProfit(2,prices))