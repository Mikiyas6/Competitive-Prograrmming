class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured] 

        for row in range(1, query_row + 1):
            cur_row = [0] * (row + 1)

            for i in range(row):
                excess = prev_row[i] - 1
                overflow = 0.5 * excess

                if excess > 0:
                    cur_row[i] += overflow
                    cur_row[i + 1] += overflow

            prev_row = cur_row

        return min(1, prev_row[query_glass])