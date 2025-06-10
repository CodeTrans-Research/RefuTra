def f_gold(arr, n):
    from queue import Queue
    from collections import deque
    
    q = deque()
    arr = arr[:n]
    arr.sort()
    q.append(arr[0])
    
    for i in range(1, n):
        now = q[0]
        if arr[i] >= 2 * now:
            q.popleft()
        q.append(arr[i])
    
    return len(q)