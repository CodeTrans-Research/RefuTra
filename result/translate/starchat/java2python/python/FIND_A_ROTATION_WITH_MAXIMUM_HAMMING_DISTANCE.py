def f_gold(arr, n):
        brr = [0] * (2 * n + 1)
        for i in range(n):
            brr[i] = arr[i]
        for i in range(n):
            brr[n + i] = arr[i]
        maxHam = 0
        for i in range(1, n):
            currHam = 0
            for j in range(i, n + i):
                if brr[j]!= arr[j - i]:
                    currHam += 1
            if currHam == n:
                return n
            maxHam = max(maxHam, currHam)
        return maxHam