class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n =len(nums)
        memo=[[-1]*(n+1) for _ in range(n) ]

        def dfs(i,j):
            if i==n:
                return 0
            if memo[i][j+1]!=-1:
                return memo[i][j+1]
            
            lis=dfs(i+1,j)

            if j ==-1 or nums[j]<nums[i]:
                lis=max(lis,1+dfs(i+1,i))

            memo[i][j+1]=lis
            return lis

        return dfs(0,-1)
            
            
            


        