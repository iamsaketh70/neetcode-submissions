class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr=0
        lc=0
        n = len(matrix)
        m = len(matrix[0])
        rr=n-1
        rc=m-1
        
        while lr <=rr:
                midr = lr+(rr-lr)//2
                if target < matrix[midr][0]:
                    rr=midr-1
                elif target > matrix[midr][m-1]:
                    lr=midr+1
                else:
                    while lc<=rc:
                        midc= lc+(rc-lc)//2
                        if matrix[midr][midc] == target:
                            return True
                        elif matrix[midr][midc] < target:
                            lc=midc+1
                        else :
                            rc=midc-1
                    return False
        return False


                    


                
                
                    



        