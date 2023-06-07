class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        lists = []
        listo = []
        for pairs in points:
            total = 0
            for nums in pairs:
                total += nums**2
            root = total**0.5
            lists.append((root,pairs))
        lists = self.merge_sort(lists)
        for p in range(k):
            listo.append(lists[p][1])
        return listo
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
