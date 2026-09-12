class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count=0,0

        for num in nums:
            if count ==0:
                res=num

            count= count+1 if num==res else count-1

        return res

