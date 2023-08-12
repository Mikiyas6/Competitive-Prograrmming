# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        listings = []
        current = lists
        for i in range(len(lists)):
            current = lists[i]
            while current:
                listings.append(current.val)
                current = current.next
        self.HeapSort(listings,len(listings))
        return self.Linked_List(listings)
    def Linked_List(self,listings):
        if len(listings) == 0:
            return
        head = ListNode(listings[-1])
        for i in range(len(listings)-2,-1,-1):
            new_node = ListNode()
            new_node.val = listings[i]
            new_node.next = head
            head = new_node
        return head

    def heapify(self,arr, n, index):
        parent_node = (index-1)//2
        
        if parent_node >= 0 and arr[index] > arr[parent_node]:
            self.swap_nodes(arr,parent_node,index)
            self.heapify(arr,n,parent_node)
        else:
            return
        
    # Function to swap nodes
    def swap_nodes(self,arr,index1,index2):
        arr[index1], arr[index2] = arr[index2], arr[index1]

    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n):
            self.heapify(arr,n,i)

    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        for i in range(n):
            self.swap_nodes(arr, 0 ,n-1-i)
            self.percolate_down(arr, 0 ,n-1-i)

    # Function used to maintain the heap order property by moving down
    def percolate_down(self,arr,index,length):
        left_node = 2*index + 1
        right_node = 2*index + 2
        
        largest = index
        if left_node < length and arr[left_node] > arr[index]:
            largest = left_node
        
        if right_node < length and arr[right_node] > arr[largest]:
            largest = right_node
            
        if largest != index:
            self.swap_nodes(arr,index,largest)
            self.percolate_down(arr,largest,length)
        else:
            return
