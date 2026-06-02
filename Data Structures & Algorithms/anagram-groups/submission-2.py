
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for string in strs:
            count = tuple(sorted(string))
            group[count].append(string)
        
        return list(group.values())