def f_gold(arr, n):
        temp = [0] * n
        small = 0
        large = n - 1
        flag = True
        for i in range(n):
            if flag:
                temp[i] = arr[large]
                large -= 1
            else:
                temp[i] = arr[small]
                small += 1
            flag = not flag
        for k in range(n):
            arr[k] = temp[k]
        return arr