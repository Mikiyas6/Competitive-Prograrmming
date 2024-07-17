class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ones_to_pick = min(numOnes, k)
        k -= ones_to_pick
        
        zeros_to_pick = min(numZeros, k)
        k -= zeros_to_pick
    
        neg_ones_to_pick = min(numNegOnes, k)
        k -= neg_ones_to_pick
        
        return ones_to_pick - neg_ones_to_pick