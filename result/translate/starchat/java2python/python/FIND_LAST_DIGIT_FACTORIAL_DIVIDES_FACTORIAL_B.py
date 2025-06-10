def f_gold(A, B):
        if A == B:
            return 1
        if (B - A) >= 5:
            return 0
        variable = 1
        for i in range(A + 1, B + 1):
            variable = (variable * (i % 10)) % 10
        return variable % 10