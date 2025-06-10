def f_gold(arr, n):
        jumps = [0] * n
        min = 0
        for i in range(n - 1, -1, -1):
            if arr[i] == 0:
                jumps[i] = sys.maxsize
            elif arr[i] >= n - i - 1:
                jumps[i] = 1
            else:
                min = sys.maxsize
                for j in range(i + 1, n + 1):
                    if j <= arr[i] + i and min > jumps[j - 1]:
                        min = jumps[j - 1]
                if min!= sys.maxsize:
                    jumps[i] = min + 1
                else:
                    jumps[i] = min
        return jumps[0]