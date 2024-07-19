class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_rows = [min(row) for row in matrix]

        max_in_cols = [max(col) for col in zip(*matrix)]
        
        lucky_numbers = [num for num in min_in_rows if num in max_in_cols]

        return lucky_numbers