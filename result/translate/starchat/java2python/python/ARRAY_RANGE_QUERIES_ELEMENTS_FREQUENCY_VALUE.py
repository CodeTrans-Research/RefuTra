def f_gold(start, end, arr):
        mp = {}
        for i in range(start, end + 1):
            mp[arr[i]] = mp.get(arr[i], 0) + 1
        count = 0
        for entry in mp.items():
            if entry[1] == max(mp.values()):
                count += 1
        return count