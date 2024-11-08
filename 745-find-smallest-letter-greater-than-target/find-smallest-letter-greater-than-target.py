class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        start = 0
        end = n-1

        def ceil(start,end,letters,target):
            if start > end:
                if start < n:
                    return letters[start]
                return letters[0]
            mid = start + (end-start)//2
            if target < letters[mid]:
                end = mid-1
            else:
                start = mid+1
            return ceil(start,end,letters,target)
        
        return ceil(start,end,letters,target)