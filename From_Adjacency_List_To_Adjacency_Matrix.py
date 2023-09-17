matrix_size = int(input())

Adjacency_Matrix = [[str(0)]*matrix_size for i in range(matrix_size)]

for i in range(matrix_size):
    row = list(map(int, input().split()))
    if row[0] != 0:
        for values in row[1:]:
            Adjacency_Matrix[i][values-1] = str(1)
    print(" ".join(Adjacency_Matrix[i]))
