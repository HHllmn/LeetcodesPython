class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minPrice = 10000000000

        for i in range(len(prices)):
            if (prices[i] < minPrice):
                minPrice = prices[i]
            else:
                potentialProfit = prices[i] - minPrice
                if (potentialProfit > profit):
                    profit = potentialProfit
  
        return profit
    
