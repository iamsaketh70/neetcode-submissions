class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard=[["."]*n for i in range(n)]
        res=[]
        negativediag=set()
        positivediag=set()
        col=set()

        def backtrack(r):
            if r ==n:
                copy=["".join(row) for row in chessboard]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r-c) in negativediag or (r+c) in positivediag:
                    continue
                
                col.add(c)
                negativediag.add(r-c)
                positivediag.add(r+c)
                chessboard[r][c]="Q"

                backtrack(r+1)

                col.remove(c)
                negativediag.remove(r-c)
                positivediag.remove(r+c)
                chessboard[r][c]="."
        
        backtrack(0)
        return res

            
            


        








        