def f_gold(arr, n):
        um = {}
        sum = 0
        maxLen = 0
        for i in range(n):
            sum += arr[i] == 0? -1 : 1
            if sum == 1:
                maxLen = i + 1
            else:
                if sum not in um:
                    um[sum] = i
                else:
                    if maxLen < i - um[sum]:
                        maxLen = i - um[sum]
        return maxLen