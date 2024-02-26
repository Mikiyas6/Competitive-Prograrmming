class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        
        items = sorted(zip(values, labels), reverse=True)
        label_count = defaultdict(int)
        score = 0
        selected = 0
        
        for value, label in items:
            if selected == numWanted:
                break
            if label_count[label] < useLimit:
                score += value
                label_count[label] += 1
                selected += 1
                
        return score