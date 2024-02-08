# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n = int(input())

hashmap = defaultdict(int)

for _ in range(n):
    
    name, phone_number = list(input().split())
    hashmap[name] = phone_number
    
while True:
    try:
        
        name = input().strip()
        
        if not name:
            break
        
        if name in hashmap:
            print("{}={}".format(name,hashmap[name]))
        else:
            print("Not found")
        
    except EOFError:
        break
