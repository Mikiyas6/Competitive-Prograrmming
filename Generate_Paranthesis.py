class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(open_count, close_count, path):
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count, path)
                path.pop()
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1, path)
                path.pop()

        result = []
        backtrack(0, 0, [])
        return result


        
