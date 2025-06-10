def f_gold(arr, n):
        if n < 1:
            return False
        min = getMin(arr, n)
        max = getMax(arr, n)
        if max - min + 1 == n:
            visited = [False] * n
            for i in range(n):
                if visited[arr[i] - min]!= False:
                    return False
                visited[arr[i] - min] = True
            return True
        return False