def f_gold(S, n):
        S.sort()
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if S[i] == S[j] + S[k] + S[l]:
                            return S[i]
        return float('inf')