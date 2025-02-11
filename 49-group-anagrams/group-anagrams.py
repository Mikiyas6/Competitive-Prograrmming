class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for value in strs:
            sorted_value = sorted(value)
            hashmap[''.join(sorted_value)].append(value)
        return list(hashmap.values())
