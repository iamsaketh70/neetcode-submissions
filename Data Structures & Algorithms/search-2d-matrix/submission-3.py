class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lc,rc=0,len(matrix[0])-1
        lr,rr=0,len(matrix)-1

        while lr<=rr:
            midr=lr+(rr-lr)//2
            if target < matrix[midr][0]:
                rr=midr-1
            elif target > matrix[midr][rc]:
                lr=midr+1
            else:
                while lc<=rc:
                    midc=lc+(rc-lc)//2
                    if target == matrix[midr][midc]:
                        return True
                    if target > matrix[midr][midc]:
                        lc=midc+1
                    else:
                        rc=midc-1
                return False
        return False


        