def f_gold(N):
    if N <= 6:
        return N
    
    screen = [0] * N
    for n in range(1, 7):
        screen[n - 1] = n
        
    for n in range(7, N+1):
        screen[n - 1] = max(2 * screen[n - 4], max(3 * screen[n - 5], 4 * screen[n - 6]))
    
    return screen[N - 1]