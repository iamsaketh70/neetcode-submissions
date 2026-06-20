class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=float("-inf")
        curmax,curmin=1,1
        for num in nums:
            temp=curmax
            curmax=max(curmax*num,curmin*num,num)
            curmin=min(curmin*num,temp*num,num)
            res=max(res,curmax)
        return res
        

        