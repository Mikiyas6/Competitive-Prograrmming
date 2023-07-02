class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles = sorted(piles)
        pint = []
        for i in range(len(piles)):
            pint.append(piles.pop())
        piles = pint
        total = 0
        for i in range(len(piles)/3):
            total += piles[2*i + 1]
        return total
    


        
