def f_gold(arr, n):
    sum = 0
    max_size = -1
    start_index = 0
    end_index = 0
    for i in range(n - 1):
        sum = (arr[i] == 0) * (-1) + 1
        for j in range(i + 1, n):
            if arr[j] == 0:
                sum += -1
            else:
                sum += 1
            if sum == 0 and max_size < j - i + 1:
                max_size = j - i + 1
                start_index = i
        if max_size!= -1:
            end_index = start_index + max_size - 1
            return start_index, end_index
    print("No such subarray")
    return