class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0

        i = 0
        j = len(height) - 1

        while i < j:

            area = (j - i)*min(height[i],height[j])
            max_area = max(max_area,area)

            if height[i] < height[j]:

                i += 1

            else:

                j -= 1
        
        return max_area




