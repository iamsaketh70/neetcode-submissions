class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp = [0 for i in range(len(nums))]
        # res = nums[0]
        # dp[0] = nums[0]
        # for i in range(1,len(nums)):
        #     dp[i] = max(nums[i],dp[i-1]+nums[i])
        #     res = max(res,dp[i])
        
        # return res
        submax = nums[0]
        cursum = nums[0]
        for i in range(1,len(nums)):

            if cursum <0:
                cursum =0
            cursum +=nums[i]
            submax=max(submax,cursum)
        return submax
            
            


            
            
