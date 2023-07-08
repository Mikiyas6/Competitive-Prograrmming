num_test_cases = int(input())
while num_test_cases > 0:
    n = int(input())
    weights = list(map(int, input().split()))

    left_index = -1
    right_index = n
    count_a = 0
    count_b = 0
    sum_a = 0
    sum_b = 0
    result = 0

    while count_a + count_b < n:
        if sum_a <= sum_b:
            left_index += 1
            count_a += 1
            sum_a += weights[left_index]
        else:
            right_index -= 1
            count_b += 1
            sum_b += weights[right_index]
        if sum_a == sum_b:
            result = count_a + count_b

    print(result)

    num_test_cases -= 1
