class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        
        first_str = strs[0]
        last_str = strs[-1]

        common_prefix = self.findCommonPrefix(first_str, last_str)

        return common_prefix

    def findCommonPrefix(self, first_str: str, last_str: str) -> str:
        common_prefix = ""
        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] == last_str[i]:
                common_prefix += first_str[i]
            else:
                break
        return common_prefix

            

