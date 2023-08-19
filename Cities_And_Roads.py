n = int(input())
Adjacency_Matrix = [list(map(int,input().split())) for _ in range(n)]

road_count = 0
for i in range(n):
    for j in range(i + 1, n):
        if Adjacency_Matrix[i][j] == 1:
            road_count += 1

print(road_count)
