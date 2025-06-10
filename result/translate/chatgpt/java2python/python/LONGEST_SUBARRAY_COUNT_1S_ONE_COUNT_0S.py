def f_gold(arr, n):
    um = {}
    sum_val = 0
    max_len = 0
    for i in range(n):
        sum_val += -1 if arr[i] == 0 else 1
        if sum_val == 1:
            max_len = i + 1
        elif sum_val not in um:
            um[sum_val] = i
        if sum_val - 1 in um:
            if max_len < (i - um[sum_val - 1]):
                max_len = i - um[sum_val - 1]
    return max_len