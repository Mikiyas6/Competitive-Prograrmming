class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        counter = 0

        row_length = len(strs)
        column_length = len(strs[0])

        for col in range(column_length):

            characters = []

            for row in range(row_length):

                characters.append(strs[row][col])
            
            if characters != sorted(characters):

                counter += 1
        
        return counter

