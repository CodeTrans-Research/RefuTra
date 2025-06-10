def f_gold(a, arr_size):
        lo = 0
        hi = arr_size - 1
        mid = 0
        temp = 0
        while mid <= hi:
            if a[mid] == 0:
                temp = a[lo]
                a[lo] = a[mid]
                a[mid] = temp
                lo += 1
                mid += 1
            elif a[mid] == 1:
                mid += 1
            else:
                temp = a[mid]
                a[mid] = a[hi]
                a[hi] = temp
                hi -= 1