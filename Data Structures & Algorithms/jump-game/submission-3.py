class Solution:
    def canJump(self, nums: List[int]) -> bool:
        shift = nums[0]
        def dfs(i):
            if i >=len(nums):
                return False
            if i == len(nums)-1:
                return True
            shift = nums[i]
            if shift == 0:
                return False
            
            for jump in range(1,shift+1):
                if dfs(i+jump):
                    return True
            return False

        return dfs(0)