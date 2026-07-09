class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        if(k==1):
            return 0

        nums.sort()
        min_difference = nums[k-1] - nums[0]

        for i in range(k,len(nums)):
            if (nums[i] - nums[i-k+1] < min_difference):
                min_difference = nums[i] - nums[i-k+1]
        
        return min_difference
            




        