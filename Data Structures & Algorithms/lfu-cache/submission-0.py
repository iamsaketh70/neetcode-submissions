class Listnode:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.freq=1
        self.prev=None
        self.next=None

class Linkedlist:
    def __init__(self):
        self.left=Listnode(0,0)
        self.right=Listnode(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.size=0
    def length(self):
        return self.size

    def pushRight(self,node):
        pre,nxt=self.right.prev,self.right
        node.prev=pre
        node.next=nxt
        pre.next=nxt.prev=node
        self.size+=1

    def pop(self,node):
        pre,nxt=node.prev,node.next
        pre.next=nxt
        nxt.prev=pre
        node.next=node.right=None
        self.size-=1
    
    def popleft(self):
        if self.length()==0:
            return None
        node=self.left.next
        self.pop(node)
        return node
        
class LFUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.lfucnt=0
        self.nodemap={}
        self.listmap=defaultdict(Linkedlist)

    def counter(self,node):
        cnt=node.freq
        self.listmap[cnt].pop(node)
        if cnt==self.lfucnt and self.listmap[cnt].length()==0:
            self.lfucnt+=1

        node.freq+=1
        self.listmap[node.freq].pushRight(node)
        
    def get(self, key: int) -> int:
        if key not in self.nodemap:
            return -1
        node=self.nodemap[key]
        self.counter(node)
        return node.val      

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return
        if key in self.nodemap:
            node=self.nodemap[key]
            self.counter(node)
            node.val=value
        
        if self.cap==len(self.nodemap):
            node=self.listmap[self.lfucnt].popleft()
            self.nodemap.pop(node.key)

        node=Listnode(key,value)
        self.nodemap[key]=node
        self.lfucnt=1
        self.listmap[self.lfucnt].pushRight(node)
        

        


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)