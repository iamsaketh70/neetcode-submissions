class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r,c=len(matrix),len(matrix[0])
        firstrowzero=False
        firstcolzero=False

        for i in range(0,c):
            if matrix[0][i]==0:
                firstcolzero=True
            

        for j in range(0,r):
            if matrix[j][0]==0:
                firstrowzero=True

        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1,r):
            for j in range(1,c):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0

        if firstcolzero==True:
            for i in range(c):
                matrix[0][i]=0

        if firstrowzero:
            for i in range(r):
                matrix[i][0]=0


        
        