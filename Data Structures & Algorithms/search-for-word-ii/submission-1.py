class Trie:
    def __init__(self):
        self.children={}
        self.word=None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Trie()
        for w in words:
            node=root
            for c in w:
                if c not in node.children:
                    node.children[c]=Trie()
                node=node.children[c]

            node.word=w

        row,col=len(board),len(board[0])
        res=set()
        def dfs(r,c,node):
            if (r>=row or c>=col or r<0 or c<0):
                return
            char=board[r][c]

            if char not in node.children:
                return

            nextnode=node.children[char]
            if nextnode.word:
                res.add(nextnode.word)

            board[r][c]="#"
            dfs(r+1,c,node.children[char])
            dfs(r-1,c,node.children[char])
            dfs(r,c+1,node.children[char])
            dfs(r,c-1,node.children[char])
            board[r][c]=char
            
        for r in range(row):
            for c in range(col):
                dfs(r,c,root)
        return list(res)



            

            




        