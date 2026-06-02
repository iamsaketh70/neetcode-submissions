class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)
        # return -1
        # n = len(nums)
        # low,high=1,n-1
        # while low< high:
        #     mid = low+(high-low)//2
        #     equal=sum(1 for num in nums if num<=mid)

        #     if equal<=mid:
        #         low=mid+1
        #     else:
        #         high=mid
        # return low
        n = len(nums)
        slow,fast=0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2=0
        while True:
            slow= nums[slow]
            slow2=nums[slow2]
            if slow == slow2:
                return slow









        