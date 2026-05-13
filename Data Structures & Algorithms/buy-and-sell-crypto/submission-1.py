class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        We are given a list of prices
        iterate through each of them and check for the max profit is changed 
        We could iterate for each one but should be fine to just always choose the lower price as buy
        """
        profit = 0
        buy_price = prices[0]
        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            profit = max(profit, price-buy_price)

        return profit