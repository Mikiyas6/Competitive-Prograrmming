class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0

        i = 0
        j = len(height) - 1

        while i < j:

            if height[i] < height[j]:

                new_area = height[i] * (j-i)
                max_area = max(max_area,new_area)
                i += 1
            
            else:

                new_area = height[j] * (j-i)
                max_area = max(max_area,new_area)
                j -= 1
            
        return max_area


