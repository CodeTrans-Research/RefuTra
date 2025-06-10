def f_gold(arr, n, k):
    um = {}
    sum = [0] * n
    curr_rem = 0
    maxSum = 0
    sum[0] = arr[0]
    
    for i in range(1, n):
        sum[i] = sum[i - 1] + arr[i]
    
    for i in range(n):
        curr_rem = sum[i] % k
        if curr_rem == 0:
            if maxSum < sum[i]:
                maxSum = sum[i]
        elif curr_rem not in um:
            um[curr_rem] = i
        elif maxSum < (sum[i] - sum[um[curr_rem]]):
            maxSum = sum[i] - sum[um[curr_rem]]
    
    return maxSum // k