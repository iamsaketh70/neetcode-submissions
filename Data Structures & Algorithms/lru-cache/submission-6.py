class double:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.left,self.right=double(0,0),double(0,0)
        self.cache={}
        self.left.nxt=self.right
        self.right.prev=self.left

    def remove(self,node):
        pre,nxt=node.prev,node.next
        pre.next=nxt
        nxt.prev=pre

    def insert(self,node):
        pre,nxt=self.right.prev,self.right
        pre.next,nxt.prev=node,node
        node.prev=pre
        node.next=nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node=double(key,value)
        self.cache[key]=node
        self.insert(node)
        if self.cap<len(self.cache):
            lru=self.left.next
            self.remove(lru)

            del self.cache[lru.key]


        
        
