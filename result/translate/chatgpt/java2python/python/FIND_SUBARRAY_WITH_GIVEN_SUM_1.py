def f_gold(arr, n, sum):
    curr_sum = arr[0]
    start = 0
    for i in range(1, n):
        while curr_sum > sum and start < i - 1:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == sum:
            p = i - 1
            print("Sum found between indexes " + str(start) + " and " + str(p))
            return 1
        if i < n:
            curr_sum += arr[i]
    print("No subarray found")
    return 0