class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n= len(prices)
        cheapest_day=prices[0]
        max_profit= 0

        for i in range(1,n):
            cheapest_day= min(cheapest_day, prices[i])

            max_profit= max(max_profit, prices[i]- cheapest_day)

        return max_profit
            
        

        