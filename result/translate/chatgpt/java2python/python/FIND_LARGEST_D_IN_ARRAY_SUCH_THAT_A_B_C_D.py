def f_gold(S, n):
    found = False
    S.sort()
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if i == j:
                continue
            for k in range(j + 1, n):
                if i == k:
                    continue
                for l in range(k + 1, n):
                    if i == l:
                        continue
                    if S[i] == S[j] + S[k] + S[l]:
                        found = True
                        return S[i]
    if not found:
        return float('inf')
    return -1