class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        N = len(nums)

        # convert big number to smaller one
        sum_nums = sum(nums)
        layer_deleted = target // sum_nums
        target = target - layer_deleted * sum_nums
        
        def get_size(i, j):
            real_i = i[1] + (0 if i[0] == 0 else N)
            real_j = j[1] + (0 if j[0] == 0 else N)
            return real_j - real_i + 1
        def i_bigger_j(i, j):
            if i[0] < j[0]:
                return False
            return i[1] > j[1]
        def move(i):
            i[1] += 1
            if i[1] == N:
                i[0] += 1
                i[1] = 0

        # sliding window
        smallest_size = None
        # (layer (0 or 1), index in that layer)
        i, j = [0, 0], [0, 0]
        cur_sum = 0
        while j[0] <= 1 and j[1] < N:
            # update the result
            cur_sum += nums[j[1]]

            # Increase i
            while cur_sum >= target and not i_bigger_j(i, j):
                # print(i, j, cur_sum)
                if cur_sum == target:
                    # update result
                    if smallest_size == None:
                        smallest_size = get_size(i, j)
                    else:
                        smallest_size = min(smallest_size, get_size(i, j))

                cur_sum -= nums[i[1]]
                move(i)
            
            # Increase j at end of loop
            move(j)
        
        if smallest_size == None:
            return -1
        else:
            return smallest_size + layer_deleted * N