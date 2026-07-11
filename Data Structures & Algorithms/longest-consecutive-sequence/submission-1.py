class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        maxlen=0

        for i in range(len(nums)):
            if nums[i]-1 not in num_set:
                current=nums[i]
                length=1

                while current+1 in num_set:
                    current+=1
                    length+=1

                maxlen=max(maxlen,length)
        return maxlen



        