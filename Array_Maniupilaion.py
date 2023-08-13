def arrayManipulation(n, queries):
    # Write your code here
    lists1 = [0] * (n+1)
    for value in queries:
        start = value[0] - 1
        end = value[1]
        offset = value[2]
        lists1[start] += offset
        if end < len(lists1):
            lists1[end] -= offset
    total = 0
    maximum = 0
    for i in range(len(lists1)):
        total += lists1[i]
        maximum = max(total,maximum)
    return maximum
