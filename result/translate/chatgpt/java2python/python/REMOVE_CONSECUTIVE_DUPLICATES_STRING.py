def f_gold(S):
    n = len(S)
    if n < 2:
        return
    j = 0
    for i in range(1, n):
        if S[j] != S[i]:
            j += 1
            S[j] = S[i]
    
    print(S[:j+1])