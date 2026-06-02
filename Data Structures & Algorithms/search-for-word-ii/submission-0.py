class TriNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TriNode()

        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TriNode()
                node = node.children[c]
            node.word = w

        ROWS,COLS = len(board),len(board[0])
        res = set()
        def dfs(r,c,node):
            if(r<0 or c<0 or
               r>= ROWS or c>= COLS):
               return
            char = board[r][c]
            if char not in node.children:
                return 
            nextNode = node.children[char]

            if nextNode.word:
                res.add(nextNode.word)
            
            board[r][c] = "#"
            
            dfs(r+1,c,nextNode)
            dfs(r-1,c,nextNode)
            dfs(r,c+1,nextNode)
            dfs(r,c-1,nextNode)

            board[r][c] = char

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)


        return list(res)




        
            

                
            
            
            
            


            
            

        
        