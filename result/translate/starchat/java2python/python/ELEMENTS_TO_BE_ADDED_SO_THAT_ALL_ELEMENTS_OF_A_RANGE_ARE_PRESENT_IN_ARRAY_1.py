def f_gold(arr, n):
        s = set()
        count = 0
        maxm, minm = float("-inf"), float("inf")
        for i in range(n):
            s.add(arr[i])
            if arr[i] < minm:
                minm = arr[i]
            if arr[i] > maxm:
                maxm = arr[i]
        for i in range(int(minm), int(maxm)+1):
            if i not in s:
                count += 1
        return count