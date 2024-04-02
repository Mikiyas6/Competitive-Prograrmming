class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        longest = 0
        hashmap = defaultdict(int)
        max_value = 0

        for r in range(len(s)):

            hashmap[s[r]] += 1

            max_value = max(hashmap.values())

            length = r - l + 1

            number_of_replaceable_chars = length - max_value

            while number_of_replaceable_chars > k:

                hashmap[s[l]] -= 1

                l += 1

                max_value = max(hashmap.values())

                length -= 1

                number_of_replaceable_chars = length - max_value

            longest = max(longest,length)
        
        return longest
       


