def f_gold(a1, a2, a3, n1, n2, n3, sum):
        s = set()
        for i in range(n1):
            s.add(a1[i])
        al = list(s)
        for i in range(n2):
            for j in range(n3):
                if (al.count(sum - a2[i] - a3[j]) > 1 and al.index(sum - a2[i] - a3[j])!= len(al) - 1):
                    return True
        return False