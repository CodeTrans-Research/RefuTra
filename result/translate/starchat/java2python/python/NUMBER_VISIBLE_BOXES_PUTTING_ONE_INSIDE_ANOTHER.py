def f_gold(arr, n):
        arr.sort()
        q = []
        for i in range(n):
            while q and arr[i] >= 2 * q[-1]:
                q.pop()
            q.append(arr[i])
        return len(q)