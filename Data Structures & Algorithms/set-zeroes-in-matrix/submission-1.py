class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r= len(matrix)
        c=len(matrix[0])
        firstrowzero= False
        firstcolzero= False
        for j in range(c):
            if(matrix[0][j]==0):
                firstrowzero=True
        for i in range(r):
            if(matrix[i][0]==0):
                firstcolzero=True

        for i in range(r):
            for j in range(c):
                if (matrix[i][j] ==0 and i!=0 and j!=0):
                    matrix[i][0]=0
                    matrix[0][j]=0
                
        for i in range(1,r):
            for j in range(1,c):
                if(matrix[0][j] ==0 or matrix[i][0]==0):
                    matrix[i][j]=0
        if firstrowzero:
            for j in range(c):
                matrix[0][j]=0
        if firstcolzero:
            for i in range(r):
                matrix[i][0]=0
            
                


                

                    



                    








        
        