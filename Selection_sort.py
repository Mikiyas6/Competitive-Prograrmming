#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min = i
            for j in range(i+1,n):
                if arr[j] < arr[min]:
                    min = j
            self.swap(arr,i,min)
        return arr
    def swap(self,arr,x,y):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
