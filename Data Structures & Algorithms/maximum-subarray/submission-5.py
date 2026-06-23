class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[[None]*2 for i in range(len(nums))]
        def dfs(i,flag):
            if i >= len(nums):
                return 0 if flag == True else -1e6
            if dp[i][flag] is not None:
                return dp[i][flag]

            if flag == True:
                dp[i][flag]=max(0,nums[i]+dfs(i+1,True))
            else:
                dp[i][flag]=max(dfs(i+1,flag),nums[i]+dfs(i+1,True))

            return dp[i][flag]

        return dfs(0,False)


            

            
        