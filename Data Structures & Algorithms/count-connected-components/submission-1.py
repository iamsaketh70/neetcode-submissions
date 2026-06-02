class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        premap={i:[] for i in range(n)}
        for node,nei in edges:
            premap[node].append(nei)
            premap[nei].append(node)
        

        visited = set()

        def dfs(node):

            if node in visited:
                return 

            visited.add(node)

            for nei in premap[node]:
                dfs(nei)
    
        res = 0   

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res


            





        