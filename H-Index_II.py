class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start = 0
        end = len(citations) - 1
        middle = 0
        while end >= start:
            if citations[start] > len(citations[start:]):
                return len(citations[start:])
            if citations[start] == len(citations[start:]):
                return citations[start]
            elif citations[end] == len(citations[end:]):
                return citations[end]
            else:
                middle = start + (end - start)//2
                if citations[middle] == len(citations[middle:]):
                    return citations[middle]
                elif citations[middle] > len(citations[middle:]) and citations[middle-1] < len(citations[middle-1:]):
                    return len(citations[middle:])
                elif citations[middle] > len(citations[middle:]):
                    end = middle - 1
                elif citations[middle] < len(citations[middle:]):
                    start = middle + 1
                elif citations[middle-1] < len(citations[middle-1:]) and citations[middle+1] > len(citations[middle+1:]):
                    return len(citations[middle:])
        return 0
