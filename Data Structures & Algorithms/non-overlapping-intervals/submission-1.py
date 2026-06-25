class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=0
        intervals.sort()
        endinterval=intervals[0][1]

        for start,end in intervals[1:]:
            if start>=endinterval:
                endinterval=end
            else:
                res+=1
                endinterval=min(endinterval,end)
        return res


        