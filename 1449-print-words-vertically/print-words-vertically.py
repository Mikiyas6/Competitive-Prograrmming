class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        max_length = 0
        for word in words:
            max_length = max(max_length,len(word))
        result = []
        for j in range(max_length):
            string = []
            for i in range(len(words)):
                string.append(words[i][j] if j < len(words[i]) else " ")
            result.append(("".join(string)).rstrip(" "))
        return result