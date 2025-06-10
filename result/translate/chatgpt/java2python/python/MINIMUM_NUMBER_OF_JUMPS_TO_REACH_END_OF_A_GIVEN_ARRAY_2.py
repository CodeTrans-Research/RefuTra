def f_gold(arr, n):
    jumps = [0] * n
    jumps[n - 1] = 0
    for i in range(n - 2, -1, -1):
        if arr[i] == 0:
            jumps[i] = float('inf')
        elif arr[i] >= n - i - 1:
            jumps[i] = 1
        else:
            min_val = float('inf')
            for j in range(i + 1, n):
                if j <= arr[i] + i:
                    if min_val > jumps[j]:
                        min_val = jumps[j]
            if min_val != float('inf'):
                jumps[i] = min_val + 1
            else:
                jumps[i] = min_val
    return jumps[0]