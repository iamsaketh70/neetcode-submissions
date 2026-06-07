class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        total =0
        subset=[]
        def dfs(i,curr,total):
            if target==total:
                subset.append(curr.copy())
                return
            elif i >= len(candidates) or total > target:
                return
            #chooosing the element
            curr.append(candidates[i])
            dfs(i+1,curr,total+candidates[i])

            curr.pop()

            while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
                i+=1

            dfs(i+1,curr,total)
        
        dfs(0,[],0)
        return subset
            
                

        