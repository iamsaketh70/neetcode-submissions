class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)
        # return -1
        n = len(nums)
        low,high=1,n-1
        while low< high:
            mid = low+(high-low)//2
            equal=sum(1 for num in nums if num<=mid)

            if equal<=mid:
                low=mid+1
            else:
                high=mid
        return low









        