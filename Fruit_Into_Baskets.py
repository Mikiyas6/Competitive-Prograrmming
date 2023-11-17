class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        dictionary = defaultdict(int)
        max_length = 0

        for r in range(len(fruits)):

            dictionary[fruits[r]] += 1

            while len(dictionary) > 2:

                dictionary[fruits[l]] -= 1

                if dictionary[fruits[l]] == 0:

                    dictionary.pop(fruits[l])

                l += 1

            max_length = max(max_length,r-l+1)

        return max_length
