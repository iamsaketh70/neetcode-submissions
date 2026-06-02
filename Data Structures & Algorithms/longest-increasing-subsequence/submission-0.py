class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo={}
        memo =[[-1]*(len(nums)+1) for _ in range(len(nums))]
        def dfs(i,j):
            if i == len(nums):
                return 0
            if memo[i][j+1]!= -1:
                return memo[i][j+1]
            
            lis = dfs(i+1,j)

            if j == -1 or nums[j]<nums[i]:
                lis = max(lis,1+dfs(i+1,i))
            



            memo[i][j+1] = lis
            return lis
        
        return dfs(0,-1)
        



            
            
            

        
        