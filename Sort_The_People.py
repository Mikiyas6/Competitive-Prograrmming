class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(names)

        for i in range(len(names)):
            swapped = False

            for j in range(0, n-i-1):
                if heights[j+1] > heights[j]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
                    swapped = True

            if not swapped:
                break
        
        return names
        

