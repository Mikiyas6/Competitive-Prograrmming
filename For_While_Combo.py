def for_while_combo(arr1,arr2):
    
    n1 = len(arr1)
    n2 = len(arr2)
    
    counter = 0
    
    j = 0
    
    output = []
    
    for i in range(n2):
        
        flag = False
        
        while j < n1:
            
            if arr2[i] > arr1[j]:
                
                print(arr2[i],arr1[j])
                counter += 1
                j += 1
            
            else:
                
                output.append(counter)
                flag = True
                break
        
        if not flag:
            output.append(counter)
                
    return output

arr1 = [2,2,5,6]
arr2 = [3,4,6,8]

print(for_while_combo(arr1,arr2))
        
        
