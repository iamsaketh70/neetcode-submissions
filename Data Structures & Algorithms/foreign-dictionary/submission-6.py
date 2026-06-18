class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        premap={}
        for word in words:
            for c in word:
                premap[c]=set()
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            if len(word2)<len(word1) and word1[:len(word2)]==word2:
                return ""
            for j in range(min(len(word1),len(word2))):
                if word1[j]!=word2[j]:
                    premap[word1[j]].add(word2[j])
                    break
        visited={}
        res=[]

        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c]=True

            for nei in premap[c]:
                if dfs(nei):
                    return True
            visited[c]=False

            res.append(c)

        for c in premap:
            if dfs(c):
                return ""



        res.reverse()
        return "".join(res)






            



        