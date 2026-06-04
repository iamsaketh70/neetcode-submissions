class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        self.stones=[-s for s in stones]
        if len(self.stones)==0:
            return 0
        heapq.heapify(self.stones)
        while len(self.stones)>1:
            first=-heapq.heappop(self.stones)
            second=-heapq.heappop(self.stones)
            bal=abs(first-second)
            if bal !=0:
                heapq.heappush(self.stones,-bal)
        return -self.stones[0]  if self.stones else 0





        


        