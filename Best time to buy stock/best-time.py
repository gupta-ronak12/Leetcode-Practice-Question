class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0

        for price in prices[1:]:
            min_so_far = min(min_so_far, price)
            max_profit = max(max_profit, price - min_so_far)

        return max_profit