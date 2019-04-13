'''

Python solution to https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Runtime beats 98.93 % of python3 submissions. (At time of submission 13/4/19)

'''



def maxProfit(prices):
        profit = 0
        for i in range(1, len(prices)): 
            if (prices[i] - prices[i-1] > 0): 
                profit = profit + (prices[i] - prices[i-1])  
        return profit
