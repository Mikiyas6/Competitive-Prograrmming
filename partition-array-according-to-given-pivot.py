class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        smaller, equal, greater = [], [], []

        for value in nums:

            if value < pivot:

                smaller.append(value)
            
            elif value > pivot:

                greater.append(value)
            
            else:

                equal.append(value)
        
        return smaller + equal + greater
