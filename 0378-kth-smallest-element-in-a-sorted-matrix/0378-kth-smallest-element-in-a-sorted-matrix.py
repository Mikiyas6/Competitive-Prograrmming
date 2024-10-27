
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rowCount = len(matrix)
        min_heap = []

        # Push the first element of each row into the minHeap
        for i in range(min(rowCount, k)):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))

        numbers_checked = 0
        smallest_element = 0

        while min_heap:
            # Get the smallest element from the heap
            smallest_element, row_index, col_index = heapq.heappop(min_heap)
            numbers_checked += 1

            # If we've checked k elements, return the k-th smallest element
            if numbers_checked == k:
                break

            # If there is a next element in the current row, add it to the heap
            if col_index + 1 < len(matrix[row_index]):
                heapq.heappush(min_heap, (matrix[row_index][col_index + 1], row_index, col_index + 1))

        return smallest_element