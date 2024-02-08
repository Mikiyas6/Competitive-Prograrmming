#User function Template for python3
from collections import Counter
def isSubset( a1, a2, n, m):
    
    if len(a2) > len(a1):
        
        return "No"
    
    hashmap_a1 = Counter(a1)
    
    hashmap_a2 = Counter(a2)
    
    for value in hashmap_a2:
        
        if hashmap_a1[value] < hashmap_a2[value] or value not in hashmap_a1:
            
            return "No"
    
    return "Yes"
            
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
