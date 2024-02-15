class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        changes = sorted(zip(indices, sources, targets), reverse=True)
        for index, source, target in changes:
            if s[index:index+len(source)] == source:
                s = s[:index] + target + s[index+len(source):]
        return s