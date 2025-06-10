def f_gold(a, n):
        total = 1
        i=2 
        while i<(n+1)+1 :
            total += i
            total -= a[i - 2]
            i += 1
        return total
