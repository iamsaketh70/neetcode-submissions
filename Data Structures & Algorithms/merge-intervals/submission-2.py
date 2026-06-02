class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort()
        # i =0
        # while i < len(intervals)-1:
        #     if (intervals[i][1] >= intervals[i+1][0]):
        #         intervals[i]= [min(intervals[i][0],intervals[i+1][0]),max(intervals[i][1],intervals[i+1][1])]
        #         intervals.pop(i+1)
        #     else:
        #         i = i+1
        # return intervals
        intervals.sort()
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<= res[-1][1]:
                res[-1][1] = max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        return res


