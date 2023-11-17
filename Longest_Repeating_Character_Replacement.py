class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        res = 0
        dictionary = {}
        max_frequency = 0

        for r in range(len(s)):

            dictionary[s[r]] = 1 + dictionary.get(s[r],0)
            max_frequency = max(max_frequency,dictionary[s[r]])
            diff = ( r - l + 1) - max_frequency

            while diff > k:

                dictionary[s[l]] -= 1
                l += 1
                diff = ( r - l + 1) - max_frequency

            res = max(res, r - l + 1)
        
        return res

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
        
#         l = 0
#         longest = 0
#         hashmap = defaultdict(int)

#         for r in range(len(s)):

#             hashmap[s[r]] += 1

#             max_value = max(hashmap.values())

#             length = r - l + 1

#             number_of_replaceable_chars = length - max_value

#             while number_of_replaceable_chars > k:

#                 hashmap[s[l]] -= 1

#                 l += 1

#                 max_value = max(hashmap.values())

#                 length = r - l + 1

#                 number_of_replaceable_chars = length - max_value
  
#             longest = max(longest,length)
        
#         return longest
       





