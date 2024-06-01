class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        from sortedcontainers import SortedList

        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        max_sum = float('-inf')

        # Iterate over all pairs of columns
        for left in range(n):
            # Initialize a row sums array
            row_sums = [0] * m
            
            for right in range(left, n):
                # Update row sums with the current column
                for i in range(m):
                    row_sums[i] += matrix[i][right]
                
                # Now we need to find the maximum subarray no larger than k
                max_subarray_sum = float('-inf')
                current_sum = 0
                sorted_sums = SortedList([0])
                
                for sum_ in row_sums:
                    current_sum += sum_
                    # We want to find the smallest sum in sorted_sums such that current_sum - that_sum <= k
                    target = current_sum - k
                    idx = sorted_sums.bisect_left(target)
                    if idx < len(sorted_sums):
                        max_subarray_sum = max(max_subarray_sum, current_sum - sorted_sums[idx])
                    # Insert the current sum into the sorted list
                    sorted_sums.add(current_sum)
                
                max_sum = max(max_sum, max_subarray_sum)
        
        return max_sum