class Solution(object):
    def maxProfit(self,prices,fees):
        """
        :type max_k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        for i in range(n):
                if( i == 0):
                    dptable[i][1] = -prices[i]
                    continue
                dptable[i][0] = max(dptable[i - 1][0], dptable[i - 1][1] + prices[i])
                dptable[i][1] = max(dptable[i - 1][1], - prices[i])

        return dptable[n - 1][0]


prices = [1, 3, 2, 8, 4, 9]
fees = 2
mySolution = Solution()
print(mySolution.maxProfit(prices,fees))