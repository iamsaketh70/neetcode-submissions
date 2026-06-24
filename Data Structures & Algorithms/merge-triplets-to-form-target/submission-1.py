class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good=set()
        for triple in triplets:
            if triple[0]>target[0]or triple[1]>target[1] or triple[2]>target[2]:
                continue
            
            for i,v in enumerate(triple):
                if v == target[i]:
                    good.add(i)
        return len(good)==3




        