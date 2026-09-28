class FreqStack:

    def __init__(self):
        self.count={}
        self.maxcount=0
        self.stack={}

    def push(self, val: int) -> None:
        self.count[val]=self.count.get(val,0)
        self.count[val]+=1
        if self.count[val]>self.maxcount:
            self.maxcount=self.count[val]
            self.stack[self.count[val]]=[]
        self.stack[self.count[val]].append(val) 

    def pop(self) -> int:
        res=self.stack[self.maxcount].pop()
        self.count[res]-=1
        if not self.stack[self.maxcount]:
            self.maxcount-=1
        return res


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()