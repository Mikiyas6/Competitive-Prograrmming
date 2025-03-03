class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for row in image:
            row = row[::-1]
            new_row = [value^1 for value in row]
            result.append(new_row)
        return result