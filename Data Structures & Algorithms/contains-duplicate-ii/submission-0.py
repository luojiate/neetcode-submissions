class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):
            
            # 找到了
            if num in window:
                return True
            
            # 裝新的
            window.add(num)

            # 淘汰舊的
            if len(window) > k:
                window.remove(nums[i - k])

        return False