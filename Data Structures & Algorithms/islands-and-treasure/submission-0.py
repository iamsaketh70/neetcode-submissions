class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row,col=len(grid),len(grid[0])
        q=deque()
        visit=set()
        def addroom(r,c):
            if (r<0 or c<0 or r>=row or c>=col or grid[r][c]==-1 or (r,c) in visit):
                return 
            visit.add((r,c))
            q.append([r,c])




        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    q.append([i,j])
                    visit.add((i,j))

        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)
            dist+=1
            











        