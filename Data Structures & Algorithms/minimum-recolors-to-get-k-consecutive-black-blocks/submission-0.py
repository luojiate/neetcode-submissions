class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 1. 初始化：計算前 k 個元素中 'W' 的數量
        whites_in_bag = blocks[:k].count("W")
        min_whites = whites_in_bag

        # 2. 袋子開始往右滑動
        for i in range(k, len(blocks)):
            
            if blocks[i] == "W":
                whites_in_bag += 1

            if blocks[i - k] == "W":
                whites_in_bag -= 1

            min_whites = min(min_whites, whites_in_bag)

        return min_whites