class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = self.merge_sort(intervals)
        print(intervals)
        i = 0
        while i < len(intervals) - 1:
            less = intervals[i][0]
            if intervals[i+1][1] > intervals[i][1]:
                greater = intervals[i+1][1]
            else:
                greater = intervals[i][1]
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = [less,greater]
                intervals.pop(i+1)
                i -= 1
            i += 1
        return intervals
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)
        return self.merges(left_half, right_half)


    def merges(self,left, right):
        merged = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged
    
