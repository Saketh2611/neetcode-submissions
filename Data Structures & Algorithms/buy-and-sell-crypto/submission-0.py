class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        sell = 0
        i = 1
        max_profit = 0
        while i < len(prices):
            if prices[i] < prices[buy]  :  
                buy = i 
                sell = i 
                if prices[sell] - prices[buy] > max_profit : 
                    max_profit =  prices[sell] - prices[buy]
                i += 1
            elif prices[i] > prices[sell] :
                sell = i 
                if prices[sell] - prices[buy] > max_profit : 
                    max_profit =  prices[sell] - prices[buy]
                i += 1 
            else : 
                i += 1
        return max_profit 


        