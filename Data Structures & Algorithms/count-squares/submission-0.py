class CountSquares:

    def __init__(self):
        self.points=defaultdict(int)

    def add(self, point: List[int]) -> None:
        x1,y1=point
        self.points[(x1,y1)]+=1


    def count(self, point: List[int]) -> int:
        x1,y1=point
        res=0

        for point,diag in self.points.items():
            x2,y2=point

            if abs(x1-x2)!=abs(y1-y2) or x1==x2 or y1==y2:
                continue
            
            res+=(diag*self.points.get((x1,y2),0)*self.points.get((x2,y1),0))
        return res
        
