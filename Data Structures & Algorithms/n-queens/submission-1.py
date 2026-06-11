class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        chessboard=[["."]*n for i in range(n)]
        positivediag=set()
        negativediag=set()
        col=set()

        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in chessboard]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in positivediag or (r-c) in negativediag:
                    continue
                
                col.add(c)
                positivediag.add(r+c)
                negativediag.add(r-c)
                chessboard[r][c]="Q"

                backtrack(r+1)

                col.remove(c)
                positivediag.remove(r+c)
                negativediag.remove(r-c)
                chessboard[r][c]="."
        backtrack(0)
        return res


                


        