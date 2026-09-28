class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        found=False

        while l<=r:
            mid=(l+r)//2
            if target<nums[mid]:
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
            elif nums[mid]==target:
                return mid
        return l



        