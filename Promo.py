length, num_queries = map(int, input().split())
values = list(map(int, input().split()))
values.sort()
prefix_sum = [0] * (length + 1)
for i in range(1, length + 1):
    prefix_sum[i] = prefix_sum[i - 1] + values[i - 1]

while num_queries > 0:
    x, y = map(int, input().split())
    result = prefix_sum[length - x + y] - prefix_sum[length - x]
    print(result)
    num_queries -= 1
