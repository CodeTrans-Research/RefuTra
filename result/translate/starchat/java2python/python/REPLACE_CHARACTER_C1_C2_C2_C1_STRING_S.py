def f_gold(s, c1, c2):
        arr = list(s)
        l = len(arr)
        for i in range(l):
            if arr[i] == c1:
                arr[i] = c2
            elif arr[i] == c2:
                arr[i] = c1
        return ''.join(arr)