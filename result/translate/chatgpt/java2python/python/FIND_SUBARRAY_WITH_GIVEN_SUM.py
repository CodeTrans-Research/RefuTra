def f_gold(arr, n, sum):
    for i in range(n):
        curr_sum = arr[i]
        for j in range(i + 1, n + 1):
            if curr_sum == sum:
                p = j - 1
                print("Sum found between indexes " + str(i) + " and " + str(p))
                return 1
            if curr_sum > sum or j == n:
                break
            curr_sum += arr[j]
    print("No subarray found")
    return 0