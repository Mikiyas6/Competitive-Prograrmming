class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        hashset = set(nums)
        result = []

        def check(string):
            if ''.join(string) not in hashset:
                result.append("".join(string))
                return True

        def dfs(string):
            if len(string) == n:
                if check(string[:]):
                    return True
                return False
            
            return dfs(string+["0"]) or dfs(string+["1"])
        
        dfs([])
        return result[0]
