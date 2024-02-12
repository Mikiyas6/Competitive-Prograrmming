class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count_chars(word: str) -> Counter:
            char_count = Counter()
            for char in word:
                char_count[char] += 1
            return char_count
        
        # Get the maximum count of each character in words2
        max_char_count = Counter()
        for word2 in words2:
            max_char_count |= count_chars(word2)
        
        # Check if word in words1 is a universal word
        def is_universal(word: str) -> bool:
            word_count = count_chars(word)
            for char, count in max_char_count.items():
                if word_count[char] < count:
                    return False
            return True
        
        return [word1 for word1 in words1 if is_universal(word1)]
        