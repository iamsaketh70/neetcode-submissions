class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res = nums[0]

        # for i in range(len(nums)):
        #     cur = nums[i]
        #     res = max(res,cur)
        #     for j in range(i+1,len(nums)):
        #         cur *= nums[j]
        #         res=max(res,cur)

        # return res
        A= []
        cur =[]
        res = float('-inf')
        for i in nums:
            res = max(res,i)
            if i ==0:
                if cur:
                    A.append(cur)
                cur =[]
            else:
                cur.append(i)
        if cur:
            A.append(cur)
        
        for sub in A:
            negs= sum(1 for i in sub if i < 0)
            prod = 1
            need = negs if negs%2 == 0 else negs-1
            negs=0
            j =0
            for i in range(len(sub)):
                prod *= sub[i]
                if sub[i] < 0:
                    negs += 1
                    while negs > need:
                        prod //= sub[j]

                        if sub[j]<0:
                            negs -=1
                        j+=1
                if j<=i:
                        res = max(res,prod)

        return res
                        







        
            


        
            

        