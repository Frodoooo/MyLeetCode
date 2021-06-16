class Solution(object):
    def coinChange(self, coins, amount):
        output = [0]
        for i in range(1,amount+1):
            temps = []
            for coin in coins:
                if(i - coin >= 0):
                    if(output[i-coin]>=0):
                        temps.append(output[i-coin]+1)
            if len(temps)>0:
                output.append( min(temps))
            else:
                output.append(-1)
        return output[amount]

coins = [2]
amount = 0
test = Solution()
output = test.coinChange(coins,amount)
print(output)