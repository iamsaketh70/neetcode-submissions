class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        premap ={}
    
        for word in words:
            for c in word:
                if c not in premap:
                    premap[c]=set()
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return""
        
          

            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    premap[w1[j]].add(w2[j])
                    break
        visited ={}
        res=[]    
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            
            for nei in premap[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)

        for c in premap:
            if dfs(c):
                return""
            
        res.reverse()
        return"".join(res)


            

        
            


            
        

                
                




        







        