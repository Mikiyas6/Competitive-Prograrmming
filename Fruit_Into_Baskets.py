class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        dictionary = defaultdict(int)

        l = 0

        length = 0

        max_length = 0

        for r in range(len(fruits)):

            dictionary[fruits[r]] += 1
            length += 1

            while len(dictionary) > 2:

                dictionary[fruits[l]] -= 1

                if dictionary[fruits[l]] == 0:

                    dictionary.pop(fruits[l])

                l += 1
                length -= 1

            max_length = max(max_length,length)
        
        return max_length

        




