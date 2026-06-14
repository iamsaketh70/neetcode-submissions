class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph={i:[] for i in range(n)}
        for node,nei in edges:
            graph[node].append(nei)
            graph[nei].append(node)
        visited=set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
        res=0

        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res


            










        