def f_gold(arr, n, k):
    sum = [0] * (n + 1)
    sum[0] = 0
    sum[1] = arr[0]
    
    for i in range(2, n+1):
        sum[i] = sum[i - 1] + arr[i - 1]
    
    Q = []
    
    for i in range(1, n+1):
        for j in range(i, n+1):
            x = sum[j] - sum[i - 1]
            
            if len(Q) < k:
                Q.append(x)
            else:
                if min(Q) < x:
                    Q.remove(min(Q))
                    Q.append(x)
    
    return min(Q)