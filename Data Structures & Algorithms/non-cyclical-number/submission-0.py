class Solution:
    def isHappy(self, n: int) -> bool:
        slowpointer,fastpointer=n,self.sumofdigits(n)

        while slowpointer!=fastpointer:
            fastpointer=self.sumofdigits(fastpointer)
            fastpointer=self.sumofdigits(fastpointer)
            slowpointer=self.sumofdigits(slowpointer)

        return True if fastpointer==1 else False


    def sumofdigits(self,n):
        total=0
        while n:
            t=n%10    
            t=t**2
            total+=t
            n=n//10
        return total    
