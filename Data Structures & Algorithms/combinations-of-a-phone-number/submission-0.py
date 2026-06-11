class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        numbertochar={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz",
        }

        def backtrack(i,currstr):
            if len(currstr)==len(digits):
                res.append(currstr)
                return
            
            for c in numbertochar[digits[i]]:
                backtrack(i+1,currstr+c)
        if digits:
            backtrack(0,"")
        
        return res
            




        
            
            




        