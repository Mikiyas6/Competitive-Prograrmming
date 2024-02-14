class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid_segment(segment):
            # Check if segment is valid (between 0 and 255 and without leading zeros)
            return 0 <= int(segment) <= 255 and (len(segment) == 1 or segment[0] != '0')
        def backtrack(start, dots, path, result):
            if dots == 0:
                # Check if the remaining string is a valid segment
                if is_valid_segment(s[start:]):
                    result.append(path + s[start:])
                return
            
            for i in range(1, 4):
                if start + i < len(s) and is_valid_segment(s[start:start+i]):
                    backtrack(start+i, dots-1, path + s[start:start+i] + ".", result)
        
        result = []
        backtrack(0, 3, "", result)
        return result