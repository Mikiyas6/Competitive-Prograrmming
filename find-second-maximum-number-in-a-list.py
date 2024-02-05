if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    
    arr.sort()
    
    for i in range(len(arr)-1,-1,-1):
        
        if arr[i] != arr[i-1]:
            
            value = arr[i-1]
            
            break
    
    print(value)
        
