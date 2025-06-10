def f_gold(arr, n):
        jumps = [0] * n
        min = 0
        i=n-2 
        while i>-1 :
            if arr[i] == 0:
                jumps[i] = sys.maxsize
            elif arr[i] >= n - i - 1:
                jumps[i] = 1
            else:
                min = sys.maxsize
                j=i+1 
                while j<n and j<=arr[i]+i :
                    if (min>jumps[j]):
                        min = jumps[j - 1]
                    j += 1
                if min!= sys.maxsize:
                    jumps[i] = min + 1
                else:
                    jumps[i] = min
            i -= 1
        return jumps[0]
