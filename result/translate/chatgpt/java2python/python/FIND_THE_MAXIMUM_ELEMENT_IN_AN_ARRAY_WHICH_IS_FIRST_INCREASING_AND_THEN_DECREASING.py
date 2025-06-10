def f_gold(arr, low, high):
    max_val = arr[low]
    for i in range(low, high + 1):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val