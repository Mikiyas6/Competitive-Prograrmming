num_test_cases = int(input())
while num_test_cases > 0:
    array_length = int(input())
    array_a = list(map(int, input().split()))
    array_b = [0] * array_length
    left_index = 0
    right_index = array_length - 1
    current_index = 0
    while current_index < array_length:
        array_b[current_index] = array_a[left_index]
        current_index += 1
        left_index += 1
        if current_index >= array_length:
            break
        array_b[current_index] = array_a[right_index]
        current_index += 1
        right_index -= 1

    for p in range(array_length):
        print(array_b[p], end=' ')
    print()

    num_test_cases -= 1

