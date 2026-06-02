class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # expected = n*(n+1)//2
        # actual = sum(nums)
        # return expected-actual
        
        res = len(nums)
        for i in range(len(nums)):
            res^=i^nums[i]
        return res


        