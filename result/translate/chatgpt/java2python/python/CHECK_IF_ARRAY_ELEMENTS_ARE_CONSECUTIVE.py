def f_gold(arr, n):
    if (n < 1):
        return False
    
    min_val = min(arr)
    max_val = max(arr)
    
    if max_val - min_val + 1 == n:
        visited = [False] * n
        for i in range(n):
            if visited[arr[i] - min_val]:
                return False
            visited[arr[i] - min_val] = True
        return True
    
    return False