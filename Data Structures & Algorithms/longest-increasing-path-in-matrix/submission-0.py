class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}
        row,column=len(matrix),len(matrix[0])
        path=set()
        num=0
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            long=1
            if i+1<row and matrix[i+1][j]>matrix[i][j]:
                long=max(long,1+dfs(i+1,j))
            if i-1>=0 and matrix[i-1][j]>matrix[i][j]:
                long=max(long,1+dfs(i-1,j))
            if j+1<column and matrix[i][j+1]>matrix[i][j]:
                long=max(long,1+dfs(i,j+1))
            if j-1>=0 and matrix[i][j-1] >matrix[i][j]:
                long =max(long,1+dfs(i,j-1))
            dp[(i,j)]=long
            return dp[(i,j)]

        for i in range(row):
            for j in range(column):
                long=dfs(i,j)
                num=max(num,long)
        
        return num
                





            
            







        