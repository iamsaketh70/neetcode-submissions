class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])

        visit=set()
        q=deque()
        fresh=0
        # def addspoil(r,c):
        #     nonlocal fresh
        #     if (min(r,c)<0 or r>=row or c>=col or grid[r][c] != 1 or (r,c) in visit ):
        #         return
        #     fresh-=1
        #     visit.add((r,c))
        #     q.append([r,c])

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.append([i,j])
                    visit.add((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        time=0
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                # grid[r][c]=2
                # addspoil(r+1,c)
                # addspoil(r-1,c)
                # addspoil(r,c+1)
                # addspoil(r,c-1)
                for dr,dc in directions:
                    rr,cl=dr+r,dc+c

                    if (min(rr,cl)<0 or rr>=row or cl>=col or grid[rr][cl]!=1):
                        continue
                    grid[rr][cl]=2
                    q.append([rr,cl])
                    fresh-=1

            time+=1
        return time if fresh==0 else -1
            



                





        



        
