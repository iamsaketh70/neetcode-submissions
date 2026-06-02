class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp = [None for i in range(len(nums))]

        # shift = nums[0]
        # def dfs(i):
        #     if i >=len(nums):
        #         return False
            
        #     if i == len(nums)-1:
        #         return True
        #     if dp[i] is not None:
        #         return dp[i]
        #     shift = nums[i]
        #     if shift == 0:
        #         dp[i] = False
        #         return False
            
        #     for jump in range(1,shift+1):
        #         if dfs(i+jump):
        #             dp[i]= True
        #             return True
        #     dp[i] = False
        #     return False

        # return dfs(0)
        maxreach = nums[0]
        for i in range(len(nums)):
            if i > maxreach:
                return False
            maxreach = max(maxreach,i+nums[i])
        return True

