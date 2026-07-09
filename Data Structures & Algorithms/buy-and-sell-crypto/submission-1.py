class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        
        current_max = 0
        global_max = 0
        
        for i in range(1, len(prices)):
            # 計算今天的價差
            diff = prices[i] - prices[i-1]
            # 如果加上今天的價差比 0 還小，不如從今天重新開始計算
            current_max = max(0, current_max + diff)
            # 紀錄過程中的最大值
            global_max = max(global_max, current_max)
            
        return global_max