class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        max_profit=0
        for key,value in enumerate(prices):
            if mini>value:
                mini=value
            profit = value - mini
            if profit> max_profit:
                max_profit = profit
        return max_profit