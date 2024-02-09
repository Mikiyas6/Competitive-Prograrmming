n = int(input())

max_people = 0
current_num = 0

for _ in range(n):
    
    num_exit, num_enter = list(map(int,input().split()))
    
    current_num -= num_exit
    current_num += num_enter
    
    max_people = max(max_people,current_num)

print(max_people)
