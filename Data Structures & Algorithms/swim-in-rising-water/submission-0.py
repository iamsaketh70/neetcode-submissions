class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited=set()
        n = len(grid)
        minheap=[[grid[0][0],0,0]]
        directions=[[0,1],[1,0],[0,-1],[-1,0]]

        while minheap:
            t,r,c=heapq.heappop(minheap)
            if r==n-1 and c==n-1:
                return t

            for dr,dc in directions:
                neiR,neiC= r+dr,c+dc
                if (neiR== n or neiC==n or (neiR,neiC) in visited or neiR<0 or neiC<0):
                    continue
                visited.add((neiR,neiC))
                heapq.heappush(minheap,[max(t,grid[neiR][neiC]),neiR,neiC])

                    
        

        

        

        

        