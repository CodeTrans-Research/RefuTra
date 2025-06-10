def f_gold(s, t, n, k):
        last, cnt, new_last, size = 0, 0, 0, 0
        for ch in range(97, 123):
            cnt = 0
            for i in range(last, n):
                if s[i] == chr(ch):
                    cnt += 1
            if cnt >= k:
                for i in range(last, n):
                    if s[i] == chr(ch):
                        t[size] = chr(ch)
                        new_last = i
                last = new_last
                size += 1
        t[size] = '\0'