class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0]*(n+1)
        optimal =1
        for i in range(1,n+1):
            if optimal*2 == i:
                optimal =i
            dp[i]= 1+dp[i-optimal]
        return dp


            


            


        