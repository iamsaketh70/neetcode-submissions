

class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        # mapping ={')':'(','}':'{',']':'['}

        # for char in s:
        #     if char in mapping:
        #         if not stack or stack[-1] != mapping[char]:
        #             return False
        #         stack.pop()
        #     else:
        #         stack.append(char)

        
        # return len(stack) == 0
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            
            elif ch in "}])":
                if not stack :
                    return False
                if stack:
                    k = stack.pop()
                if ch == "}" and k != "{":
                    return False
                if ch == "]" and k != "[":
                    return False                
                if ch == ")" and k != "(":
                    return False

        return len(stack) == 0












        