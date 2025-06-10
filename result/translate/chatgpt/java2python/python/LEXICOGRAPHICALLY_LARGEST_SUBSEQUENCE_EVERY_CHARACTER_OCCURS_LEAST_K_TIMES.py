def f_gold(s, t, n, k):
    last = 0
    cnt = 0
    new_last = 0
    size = 0
    
    for ch in range(ord('z'), ord('a')-1, -1):
        cnt = 0
        for i in range(last, n):
            if s[i] == chr(ch):
                cnt += 1
                
        if cnt >= k:
            for i in range(last, n):
                if s[i] == chr(ch):
                    t[size] = chr(ch)
                    size += 1
                    new_last = i
                    
            last = new_last
            
    t[size] = '\0'