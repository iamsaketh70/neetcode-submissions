class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[False]*n for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n,1):
                if s[i] ==s[j] and (j-i <=2 or dp[i+1][j-1]):
                    dp[i][j]=True
        
        res=[]
        path=[]
        def backtrack(start):
            if start==n:
                res.append(path.copy())
                return
            for end in range(start,n):
                if dp[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end+1)
                    path.pop()
        backtrack(0)
        return res


                
                




