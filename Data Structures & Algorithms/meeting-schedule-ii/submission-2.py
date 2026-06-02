"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key= lambda i:i.start)
        minheap=[]
        for i in range(len(intervals)):
            if minheap and minheap[0] <=intervals[i].start:
                heapq.heappop(minheap)
            heapq.heappush(minheap,intervals[i].end)

        return len(minheap)

