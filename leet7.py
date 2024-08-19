
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        n = len(nums)

        if n<2:
            return nums[0]
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum+=nums[j]
                max_sum=max(max_sum,curr_sum)
        return max_sum          

        
