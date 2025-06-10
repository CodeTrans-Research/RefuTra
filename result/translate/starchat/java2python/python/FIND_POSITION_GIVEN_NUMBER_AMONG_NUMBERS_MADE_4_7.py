def f_gold(n):
        k = 0
        pos = 0
        i = 0
        while k!= len(n):
            if n[i] == '4':
                pos = pos * 2 + 1
            elif n[i] == '7':
                pos = pos * 2 + 2
            i += 1
            k += 1
        return pos