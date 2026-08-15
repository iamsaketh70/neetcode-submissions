class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for string in strs:
            name=tuple(sorted(string))
            group[name].append(string)

        return list(group.values())
        