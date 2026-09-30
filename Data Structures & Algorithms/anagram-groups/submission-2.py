class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            sorted_dict[sortedS].append(s)
        return list(sorted_dict.values())