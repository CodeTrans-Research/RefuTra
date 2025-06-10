def f_gold(arr, n):
        index = 0
        while index < n:
            if index == 0:
                index += 1
            if arr[index] >= arr[index - 1]:
                index += 1
            else:
                temp = arr[index]
                arr[index] = arr[index - 1]
                arr[index - 1] = temp
                index -= 1
        return