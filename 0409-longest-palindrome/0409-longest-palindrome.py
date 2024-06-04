class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        palindrome_length = 0
        odd_count_exists = False
        for count in char_count.values():
            if count % 2 == 0:
                palindrome_length += count
            else:
                palindrome_length += count - 1
                odd_count_exists = True

        if odd_count_exists:
            palindrome_length += 1

        return palindrome_length