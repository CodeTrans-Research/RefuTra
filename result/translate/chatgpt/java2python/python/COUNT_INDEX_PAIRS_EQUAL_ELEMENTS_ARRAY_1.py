def f_gold(arr, n):
    hm = {}
    for i in range(n):
        if arr[i] in hm:
            hm[arr[i]] += 1
        else:
            hm[arr[i]] = 1
            
    ans = 0
    for key, value in hm.items():
        count = value
        ans += (count * (count - 1)) // 2
        
    return ans