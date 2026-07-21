class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr=[]
        fin=[]

        def dfs(i,curr,res):
            if target==res:
                fin.append(curr.copy())
                return

            if i>=len(nums) or res>target:
                return

            curr.append(nums[i])
            dfs(i,curr,nums[i]+res)
            curr.pop()
            dfs(i+1,curr,res)

        
        dfs(0,[],0)
        return fin



        