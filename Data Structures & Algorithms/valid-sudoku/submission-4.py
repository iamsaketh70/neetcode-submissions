class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        cols=len(board[0])

        for i in range(n):
            seen=set()
            for j in range(cols):
                if board[j][i]==".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        

        for i in range(n):
            seen=set()
            for j in range(cols):
                if board[i][j]==".":
                    continue
                if board[i][j] in seen:
                    return False
                
                seen.add(board[i][j])


        for row in range(0,9,3):
            for col in range(0,9,3):
                seen=set()
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j]==".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
                    
        return True


