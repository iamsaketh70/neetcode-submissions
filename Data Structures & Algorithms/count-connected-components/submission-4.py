class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph={i:[] for i in range(n)}
        for node,pre in edges:
            graph[node].append(pre)
            graph[pre].append(node)
        visited=set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
        res=0   
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res





        