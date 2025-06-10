def f_gold(arr, n):
        jumps = [float('inf')] * n
        jumps[0] = 0
        for i in range(1, n):
            for j in range(0, i):
                if i <= j + arr[j] and jumps[j]!= float('inf'):
                    jumps[i] = min(jumps[i], jumps[j] + 1)
        return jumps[n - 1]