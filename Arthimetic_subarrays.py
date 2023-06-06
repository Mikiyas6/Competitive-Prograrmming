class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        booleans = []
        lists = []
        for k in range(len(l)):
            lists = nums[l[k]:r[k]+1]
            self.Bubble_sort(lists)
            flag = True
            for p in range(len(lists)):
                if p == 0:
                    diff = lists[p+1] - lists[p]
                elif p == len(lists) - 1:
                    booleans.append(flag)
                else:
                    if diff != lists[p+1] - lists[p]:
                        flag = False
        return booleans
    def Bubble_sort(self,lists):
        for i in range(len(lists)):
            for j in range(len(lists)-i):
                if j == len(lists) - i - 1:
                    break
                elif lists[j+1] < lists[j]:
                    self.swap(lists,j,j+1)
    def swap(self,lists,x,y):
        temp = lists[x]
        lists[x] = lists[y]
        lists[y] = temp
