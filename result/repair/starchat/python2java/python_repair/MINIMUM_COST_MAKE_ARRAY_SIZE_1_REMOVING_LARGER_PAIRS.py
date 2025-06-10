def f_gold(a, n):
        min = a[0]
        i=1 
        while i<len(a) :
            if a[i] < min:
                min = a[i]
            i += 1
        return (n - 1) * min
