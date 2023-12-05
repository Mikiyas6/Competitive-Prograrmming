def merger(arr1,arr2):
    
    n1 = len(arr1)
    n2 = len(arr2)
    
    i = 0
    j = 0
    
    output = []
    
    while i < n1-1 and j < n2-1:
        
        if arr1[i] <= arr2[j]:
            
            output.append(arr1[i])
            
            i += 1
        
        else:
            
            output.append(arr2[j])
            
            j += 1
    
    output.extend(arr1[i:]+arr2[j:])
    
    return output

arr1 = [10,15,22,80]
arr2 = [5,8,11,15,70,90]

print(merger(arr1,arr2))
