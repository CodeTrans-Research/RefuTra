def f_gold(arr, n):
    sum = 0
    maxsize = -1
    startindex = 0
    endindex = 0

    for i in range(n-1):
        sum = -1 if arr[i] == 0 else 1

        for j in range(i+1, n):
            if arr[j] == 0:
                sum += -1
            else:
                sum += 1

            if sum == 0 and maxsize < j - i + 1:
                maxsize = j - i + 1
                startindex = i

    endindex = startindex + maxsize - 1

    if maxsize == -1:
        print("No such subarray")
    else:
        print(startindex, "to", endindex)

    return maxsize