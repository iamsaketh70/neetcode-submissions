class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # memo={}
        # memo = [[-1]* (n+1) for _ in range(n)]
        # def dfs(i,j):
        #     if i == len(nums):
        #         return 0
            
        #     lis = dfs(i+1,j)

        #     if j == -1 or nums[j]<nums[i]:
        #         lis = max(lis,1+dfs(i+1,i))

        #     return lis
        
        # return dfs(0,-1)
        n = len(nums)
        dp =[1]*len(nums)
        for i in range(n-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    dp[i]= max(dp[i],1+dp[j])
        return max(dp)


        



            
            
            

        
        