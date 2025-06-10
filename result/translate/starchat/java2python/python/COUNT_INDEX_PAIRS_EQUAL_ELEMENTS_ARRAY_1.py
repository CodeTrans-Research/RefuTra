def f_gold(arr, n):
        hm = {}
        for i in range(n):
            if arr[i] in hm:
                hm[arr[i]] += 1
            else:
                hm[arr[i]] = 1
        ans = 0
        for key, val in hm.items():
            ans += (val * (val - 1)) // 2
        return ans