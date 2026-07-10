class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)

        for string in strs:
            same=tuple(sorted(string))
            group[same].append(string)

        return list(group.values())