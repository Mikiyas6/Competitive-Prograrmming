class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        
        def get_signature(word):
            even_chars = word[::2]
            odd_chars = word[1::2]
            even_count = [0] * 26
            odd_count = [0] * 26
            for char in even_chars:
                even_count[ord(char) - ord('a')] += 1
            for char in odd_chars:
                odd_count[ord(char) - ord('a')] += 1
            return tuple(even_count + odd_count)

        signatures = set()
        for word in words:
            signature = get_signature(word)
            signatures.add(signature)

        return len(signatures)