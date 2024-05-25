class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordSet = set(wordDict)
        memo = {}
        
        def backtrack(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [""]
            
            results = []
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    sub_sentences = backtrack(end)
                    for sub_sentence in sub_sentences:
                        if sub_sentence:
                            results.append(word + " " + sub_sentence)
                        else:
                            results.append(word)
            
            memo[start] = results
            return results
        
        return backtrack(0)