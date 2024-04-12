class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        max_area = 0
        stack = [[0,heights[0]]]

        for i in range(1,n):

            demiser = heights[i]
            new_index = i

            while stack and demiser <= stack[-1][1]:

                index, value = stack.pop()

                area = value * (i - index)

                max_area = max(max_area,area)

                new_index = index
            
            stack.append([new_index,demiser])
        
        while stack:

            index, value = stack.pop()

            area = value * (n-index)

            max_area = max(max_area,area)
        
        return max_area
        
        


