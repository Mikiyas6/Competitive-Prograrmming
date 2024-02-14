class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        def get_parts(version):
            return list(map(int, version.split('.')))

        parts1 = get_parts(version1)
        parts2 = get_parts(version2)
        
        n = max(len(parts1), len(parts2))
        parts1 += [0] * (n - len(parts1))
        parts2 += [0] * (n - len(parts2))
        
        for p1, p2 in zip(parts1, parts2):
            if p1 < p2:
                return -1
            elif p1 > p2:
                return 1
        
        return 0