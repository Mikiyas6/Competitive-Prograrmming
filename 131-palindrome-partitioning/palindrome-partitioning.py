class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
        def backtrack(start, path, result):
            if start == len(s):
                result.append(path[:])
                return
            
            for i in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:i]):
                    path.append(s[start:i])
                    backtrack(i, path, result)
                    path.pop()
        
        result = []
        backtrack(0, [], result)
        return result