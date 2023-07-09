number_of_testcases = int(input())
for i in range(number_of_testcases):
    length_of_the_array = int(input())
    nums_list = list(map(int,input().split()))
    nums_list = sorted(nums_list)
    j = 0
    while len(nums_list) > 1:
            if nums_list[j+1] - nums_list[j] <= 1:
                nums_list.remove(nums_list[j])
            else:
                j += 1
            if j >= len(nums_list)-1:
                break
    if len(nums_list) == 1:
        print("YES")
    else:
        print("NO")
