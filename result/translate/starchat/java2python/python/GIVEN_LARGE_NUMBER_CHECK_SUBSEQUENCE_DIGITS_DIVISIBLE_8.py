def f_gold(str):
        l = len(str)
        arr = [0] * l
        for i in range(l):
            arr[i] = ord(str[i]) - ord('0')
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    if arr[i] % 8 == 0:
                        return True
                    if (arr[i] * 10 + arr[j]) % 8 == 0 and i!= j:
                        return True
                    if (arr[i] * 100 + arr[j] * 10 + arr[k]) % 8 == 0 and i!= j and j!= k and i!= k:
                        return True
        return False