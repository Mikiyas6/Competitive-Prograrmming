class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        counts = [0] * (n + 1)

        # Count the number of papers for each citation count
        for citation in citations:
            counts[min(citation, n)] += 1
        
        # Iterate from right to left to find the h-index
        total_papers = 0
        for i in range(n, -1, -1):
            total_papers += counts[i]
            if total_papers >= i:
                return i
        
        return 0
