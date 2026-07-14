class double:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev,self.next=None,None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache={}
        self.left,self.right=double(0,0),double(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    
    def remove(self,node:double):
        prev,nxt=node.prev,node.next
        node.prev.next=nxt
        node.next.prev=prev

    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.next,node.prev=self.right,prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key]=double(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        
