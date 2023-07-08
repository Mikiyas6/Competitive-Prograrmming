num_test_cases = int(input())
while num_test_cases > 0:
    array_length = int(input())
    array_values = list(map(int, input().split()))
    array_values.sort()
    max_difference = array_values[-1]
    for index in range(2, array_length):
        difference = array_values[index] - array_values[index - 2]
        max_difference = min(max_difference, difference)

    print(max_difference)
    num_test_cases -= 1

