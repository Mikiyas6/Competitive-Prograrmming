class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        length = len(stones)
        for i in range(length):
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return stones[0]
            self.buildHeap(stones,len(stones))
            value1 = stones.pop(0)
            self.buildHeap(stones,len(stones))
            value2 = stones.pop(0)
            if value1 != value2:
                stones += [value1 - value2]
    # Percolate Up
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
    

    # length = len(stones)
        # for i in range(length):
        #     if len(stones) == 0:
        #         return 0
        #     if len(stones) == 1:
        #         return stones[0]
        #     stones = sorted(stones)
        #     value1, value2 = stones[-1], stones[-2]
        #     if value1 == value2:
        #         stones = stones[:len(stones)-2]
        #     else:
        #         stones[-2] = value1 - value2
        #         stones = stones[:len(stones)-1]
        
    
