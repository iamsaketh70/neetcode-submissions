class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # for i in range(len(numbers)):
        #     remain=target-numbers[i]
        #     l,r=i+1,len(numbers)-1
        #     while l <= r:
        #         mid=(l+r)//2
        #         if remain==numbers[mid]:
        #             return [i+1,mid+1]

        #         elif numbers[mid]<remain:
        #             l=mid+1
        #         else :
        #             r=mid-1

#two twoSum
        l,r=0,len(numbers)-1

        while l<r:
            cursum=numbers[l]+numbers[r]

            if cursum < target:
                l+=1
            elif cursum >target:
                r-=1

            else:
                return [l+1,r+1]





                
                
                

            
                    