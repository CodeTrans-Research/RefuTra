def f_gold(arr, n):
        s = set()
        ans = 0
        j = 0
        for i in range(n):
            while j < n and arr[j] not in s:
                s.add(arr[j])
                j += 1
            ans += (j - i) * (j - i + 1) // 2
            s.remove(arr[i])
        return ans