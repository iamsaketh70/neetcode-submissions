class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float("inf")
        L=0
        total=0
        for R in range(len(nums)):
            total+=nums[R]
            while total >= target:
                res=min(R-L+1,res)
                total=total-nums[L]
                L+=1

        return 0 if res==float("inf") else res





        