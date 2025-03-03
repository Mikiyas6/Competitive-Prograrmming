class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_string = [0]*(max(indices)+1)
        for i in range(len(s)):
            new_string[indices[i]] = s[i]
        return "".join(new_string)