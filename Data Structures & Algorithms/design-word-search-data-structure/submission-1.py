class WordDictionary:

    def __init__(self):
        self.children={}
        self.end=False
        
    def addWord(self, word: str) -> None:
        node=self
        for c in word:
            if c not in node.children:
                node.children[c]=WordDictionary()
            node=node.children[c]
        node.end=True

    def search(self, word: str) -> bool:
        node=self
        def dfs(j,node):
            cur=node
            for i in range(j,len(word)):
                c=word[i]
                if c==".":
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                    cur=cur.children[c]
            return cur.end

        return dfs(0,node)





            


            
            
            
            
            




        
