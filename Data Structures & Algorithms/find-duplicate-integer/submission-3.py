class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        first=second=0

        while True:
            second=nums[second]
            first=nums[nums[first]]
            if first==second:
                break

        second2=0
        while True:
            second=nums[second]
            second2=nums[second2]
            if second==second2:
                return second