def f_gold(arr, arr_size):
        for i in range(arr_size):
            count = 0
            for j in range(arr_size):
                if arr[i] == arr[j]:
                    count += 1
            if count % 2!= 0:
                return arr[i]
        return -1