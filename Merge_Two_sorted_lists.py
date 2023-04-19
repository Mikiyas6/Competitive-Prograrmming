# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current1 = list1
        current2 = list2
        lists1 = []
        lists2 = []
        lists3 = []
        lists4 = []
        while(current1 != None):
            lists1.append(current1.val)
            current1 = current1.next
        while(current2 != None):
            lists2.append(current2.val)
            current2 = current2.next
        for value in lists1:
            lists3.append(value)
        for value in lists2:
            lists3.append(value)
        def sorter(lists):
            for i in range(len(lists)):
                for j in range(len(lists) - 1):
                    if lists[j] > lists[j + 1]:
                        lists[j], lists[j + 1] = lists[j + 1], lists[j]
            return lists
        lists4 = sorter(lists3)
        def insert_at_the_end(lists):
            if(len(lists) == 0):
                    return None
            else:    
                value = lists[0]
                lists.pop(0)
                return ListNode(value,insert_at_the_end(lists))
        l3 = insert_at_the_end(lists4)
        return l3
            
        




        
                



        

                    
                    


                    


            


                




        
            

        
