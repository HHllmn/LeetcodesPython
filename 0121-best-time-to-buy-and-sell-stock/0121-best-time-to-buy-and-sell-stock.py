class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minPrice = prices[0]

        for i in range(1,len(prices)):
            if (prices[i] < minPrice):
                minPrice = prices[i]
            elif (prices[i] - minPrice > profit):
                profit = prices[i] - minPrice
  
        return profit
    
