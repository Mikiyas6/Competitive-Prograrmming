left, right = 0, len(arr) - k  # Initial left and right boundaries for the sliding window

    while left < right:
        mid = (left + right) // 2  # Calculate the midpoint
        if x - arr[mid] > arr[mid + k] - x:  # If the elements on the right side are closer
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]  # Return the k closest elements starting from the left boundary
