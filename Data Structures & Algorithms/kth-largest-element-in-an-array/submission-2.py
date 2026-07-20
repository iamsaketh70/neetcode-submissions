class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.minheap=[]
        self.k=k
        for num in nums:
            heapq.heappush(self.minheap,num)

            if self.k < len(self.minheap):
                heapq.heappop(self.minheap)
            

        return  self.minheap[0]
        

































        