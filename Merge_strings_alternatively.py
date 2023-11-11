class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        string = ""

        i = 0
        j = 0

        length1 = len(word1)
        length2 = len(word2)

        while i < length1 and j < length2:

            string += word1[i] + word2[j]

            i += 1
            j += 1
        
        return string + word1[i:] + word2[j:]
