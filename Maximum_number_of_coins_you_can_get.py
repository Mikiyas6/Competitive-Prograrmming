class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()

        i = 0
        j = len(piles) - 2
        total = 0

        while i < j:

            total += piles[j]
            i += 1
            j -= 2
        
        return total
             
    #     piles.sort() # O(nlogn)

    #     i = 0
    #     j = len(piles) - 1

    #     Bob, Alice, Us = [], [], []

    #     while i < j: # O(n)

    #         Alice.append(piles[j])
    #         Us.append(piles[j-1])
    #         Bob.append(piles[i])
        
    #         i += 1
    #         j -= 2
        
    #     return sum(Us)

    # # O(nlogn) + O(n) = O(nlogn)
