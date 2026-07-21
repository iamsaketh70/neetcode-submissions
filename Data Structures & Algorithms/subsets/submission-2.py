class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sublist=[]
        res=[]

        def dfs(i):
            if i>= len(nums):
                res.append(sublist.copy())
                return

            
            # take it
            sublist.append(nums[i])
            dfs(i+1)

            #skip it
            sublist.pop()

            dfs(i+1)
        
        dfs(0)
        return res


        