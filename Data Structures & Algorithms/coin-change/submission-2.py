class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo=[-1 for i in range(amount+1)]

        def dfs(i):
            if i==0:
                return 0

            if memo[i]!=-1:
                return memo[i]
            res=1e9
            
            for coin in coins:
                if (i-coin)>=0:
                    res= min(res,1+dfs(i-coin))
            memo[i]=res
            return res

        mincoins=dfs(amount)
        return -1 if mincoins >=1e9 else mincoins                




        