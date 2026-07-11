class Solution:
    def maxArea(self, heights: List[int]):
        maxarea=0
        n=len(heights)
        l,r=0,n-1
        while l<r:
            height=min(heights[l],heights[r])
            width=abs(r-l)
            area=height*width
            maxarea=max(maxarea,area)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            
        return maxarea


        