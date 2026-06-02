class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=0
        intervals.sort()
        preEnd= intervals[0][1]
        for start,end in intervals[1:]:
            if start >= preEnd:
                preEnd=end
            else:
                res+=1
                preEnd=min(end,preEnd)
        return res





        