def f_gold(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return f_gold(arr, l, mid - 1, x)
        return f_gold(arr, mid + 1, r, x)
    return -1