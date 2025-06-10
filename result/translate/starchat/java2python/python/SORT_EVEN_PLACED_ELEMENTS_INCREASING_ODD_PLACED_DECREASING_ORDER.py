def f_gold(arr, n):
        even_arr = []
        odd_arr = []
        for i in range(n):
            if i % 2!= 1:
                even_arr.append(arr[i])
            else:
                odd_arr.append(arr[i])
        even_arr.sort()
        odd_arr.sort(reverse=True)
        i = 0
        for j in range(len(even_arr)):
            arr[i] = even_arr[j]
            i += 1
        for j in range(len(odd_arr)):
            arr[i] = odd_arr[j]
            i += 1