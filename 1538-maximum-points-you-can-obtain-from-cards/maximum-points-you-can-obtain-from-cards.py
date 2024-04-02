class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)

        l = 0

        r = n - k 

        total = sum(cardPoints[n-k:])

        max_sum = total

        while r < len(cardPoints):

            total -= cardPoints[r]

            total += cardPoints[l]

            max_sum = max(max_sum,total)
        
            l += 1

            r += 1
        
        return max_sum