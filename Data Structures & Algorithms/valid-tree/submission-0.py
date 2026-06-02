class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree_map ={i:[] for i in range(n)}
        visited = set()
        for num,chi in edges:
            tree_map[num].append(chi)
            tree_map[chi].append(num)


        def dfs(num,parent):
            if num in visited:
                return False
            visited.add(num)
            for pre in tree_map[num]:
                if pre == parent:
                    continue
                if not dfs(pre,num):return False

            return True

        if not dfs(0,-1):
            return False
        return len(visited ) == n


            

        