def f_gold(arr, l, h):
    if l >= h:
        return
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        f_gold(arr, l, h - t)
        f_gold(arr, l + t, h)
        f_gold(arr, l, h - t)