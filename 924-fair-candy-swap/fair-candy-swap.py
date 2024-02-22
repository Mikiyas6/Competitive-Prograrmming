class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        set_bob = set(bobSizes)
        
        for candy in aliceSizes:
            target_bob = (sum_bob - sum_alice + 2 * candy) // 2
            if target_bob in set_bob:
                return [candy, target_bob]