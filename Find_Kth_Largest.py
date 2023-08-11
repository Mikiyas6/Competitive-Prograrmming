class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.HeapSort(nums,len(nums))
        return nums[len(nums)-k]
        
    #Heapify function to maintain heap property.
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
