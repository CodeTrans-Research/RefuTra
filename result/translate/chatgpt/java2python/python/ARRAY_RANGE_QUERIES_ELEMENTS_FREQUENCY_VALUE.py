def f_gold(start, end, arr):
    mp = {}
    for i in range(start, end+1):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    count = 0
    for key, value in mp.items():
        if key == value:
            count += 1
    return count