class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        hashmap = defaultdict(int)

        l = 0

        max_number = 0

        for r in range(len(fruits)):

            hashmap[fruits[r]] += 1

            while len(hashmap) > 2:

                hashmap[fruits[l]] -= 1

                if hashmap[fruits[l]] == 0:

                    del hashmap[fruits[l]]
                
                l += 1

            max_number = max(max_number,r-l+1)
            
        return max_number