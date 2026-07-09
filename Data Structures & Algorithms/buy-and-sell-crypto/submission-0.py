class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_day = 0     
        max_profit = 0

        # 在買入時機固定的情況下搜尋所有賣出時機
        for sell_day in range(1, len(prices)):

            # 只要有獲利可能就進入判斷
            if prices[buy_day] < prices[sell_day]:
                profit = prices[sell_day] - prices[buy_day]
                max_profit = max(max_profit, profit)

            # 沒有獲利可能就移動買入時機
            else:
                buy_day = sell_day

        return max_profit