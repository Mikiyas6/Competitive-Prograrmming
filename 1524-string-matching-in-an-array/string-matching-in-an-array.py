class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[j] not in result and words[j] in words[i]:
                    result.append(words[j])
        return result
