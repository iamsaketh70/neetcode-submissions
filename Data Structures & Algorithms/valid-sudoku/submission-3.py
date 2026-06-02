class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count={}
        n = len(board)
        cols=len(board[0])
        
        for i in range(n):
            count={}
            for j in range(cols): 
                num=board[j][i]
                if num == ".":
                    continue
                if num in count:
                    return False
                count[num] = 1


        for i in range(n):
            count ={}
            for j in range(cols):
                num=board[i][j]
                if num == ".":
                    continue
                if num in count:
                    return False
                count[num] = 1
            
        for row in range(0,9,3):
            for col in range(0,9,3):
                count={}
                for i in range(row, row+3):
                    for j in range(col,col+3):
                        num = board[i][j]
                        if num == ".":
                            continue
                        if num in count:
                            return False
                        count[num]=1
        return True














             