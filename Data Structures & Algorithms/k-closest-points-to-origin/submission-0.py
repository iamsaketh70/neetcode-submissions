class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.maxheap,self.k= [],k

        for x,y in points:
            dist=x**2 +y**2
            heapq.heappush(self.maxheap,(-dist,[x,y]))
            if len(self.maxheap) >k:
                heapq.heappop(self.maxheap)
        return [point for dist,point in self.maxheap]
            
        


            


            

            


        