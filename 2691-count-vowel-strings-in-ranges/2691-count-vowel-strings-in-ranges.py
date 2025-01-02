class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = ["a","e","i","o","u"]

        prefix_sum = [0] * len(words)
        
        for index,word in enumerate(words):

            if word[0] in vowels and word[-1] in vowels:

                prefix_sum[index] = 1
            
        cumulative = 0

        for index, value in enumerate(prefix_sum):

            cumulative += value

            prefix_sum[index] = cumulative
        
        prefix_sum = [0] + prefix_sum
        
        result = []
        
        for left, right in queries:

            result.append(prefix_sum[right+1]-prefix_sum[left])
        
        return result