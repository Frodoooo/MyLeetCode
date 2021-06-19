class Solution(object):
    def maxProfit(self,prices):
        """
        :type max_k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        for i in range(n):
            if (i == 0):
                dp0 = 0
                dp1 = -prices[i]

            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, - prices[i])


        return dp0
    """    for i in range(n):
            if( i == 0):
                dptable[i][1] = -prices[i]
                continue
            dptable[i][0] = max(dptable[i - 1][0], dptable[i - 1][1] + prices[i])
            dptable[i][1] = max(dptable[i - 1][1], - prices[i])

        return dptable[n - 1][0]"""


prices = [7,1,5,3,6,4]
mySolution = Solution()
print(mySolution.maxProfit(prices))