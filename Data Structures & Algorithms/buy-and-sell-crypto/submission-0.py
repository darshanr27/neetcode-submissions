class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0;
        transactions = [];

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] > prices[j]:
                    continue
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    transactions.append(profit)
                    max_profit = profit
        print(transactions)
        if transactions:
            return max(transactions)
        return 0