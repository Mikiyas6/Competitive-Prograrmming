class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lists = []
        tuples = ()
        totals = 0
        totals_list = []
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            else:
                pivot = arr[0]
                left = []
                right = []
                for i in range(1, len(arr)):
                    if arr[i] < pivot:
                        left.append(arr[i])
                    else:
                        right.append(arr[i])
                return quick_sort(left) + [pivot] + quick_sort(right)
        nums = quick_sort(nums)
        while (len(nums) != 0):
            tuples = (nums.pop(0),nums.pop(-1))
            lists.append(tuples)
            tuples = ()   
        for i in range(len(lists)):
            for j in range(len(lists[i])):
                totals += lists[i][j]
            totals_list.append(totals)
            totals = 0
        return max(totals_list)
