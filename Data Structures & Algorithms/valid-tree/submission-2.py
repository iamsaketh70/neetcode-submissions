class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph={i:[] for i in range(n)}
        for par,child in edges:
            graph[par].append(child)
            graph[child].append(par)
        visited =set()

        def dfs(child,par):
            if child in visited:
                return False
            visited.add(child)
            for nei in graph[child]:
                if nei==par:
                    continue
                if not dfs(nei,child): return False
            return True

        if not dfs(0,-1):
            return False
        return len(visited)==n

            



                
                
            

            

